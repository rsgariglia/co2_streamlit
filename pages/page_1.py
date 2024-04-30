import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pandas_gbq
from google.oauth2 import service_account
from google.cloud import bigquery



st.set_page_config(layout="wide", page_title="Emissions App", initial_sidebar_state="expanded")

# Define BigQuery credentials
#credentials = st.secrets["gcp_service_account"]
#project_id = credentials["project_id"]




# Define BigQuery credentials
#credentials = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(credentials=credentials)
#project_id = credentials["project_id"]
project_id = st.secrets["gcp_service_account"]["project_id"]


# Perform query using pandas-gbq
@st.cache_data(ttl=86400, show_spinner=False)
def run_query_forecast():
    # Define the query
    query = """
    SELECT mapped_BE_material, month_year, total_waste_volume_tonnes, saved_emissions_factor, average_cost_material, average_revenue_material
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.savings_forecast_cost`
    """
    # Read data directly into DataFrame
    return pandas_gbq.read_gbq(query, project_id = project_id, credentials=credentials)

# Read data using the cached function
savings_forecast = run_query_forecast()



def calculate_savings(selected_material, waste_reduction_percentage):
    
    # Filter data for selected material
    filtered_data = savings_forecast[savings_forecast["mapped_BE_material"] == selected_material]
    
    if not filtered_data.empty:
        # Calculate the average waste volume
        avg_waste_volume = filtered_data['total_waste_volume_tonnes'].mean()
        
        # Get the emission factor
        saved_emission_factor = filtered_data.iloc[0]['saved_emissions_factor']  # Assuming it's the same for all rows
        
        # Calculate CO2 savings
        avg_co2_savings = avg_waste_volume * saved_emission_factor
        
        # Check if the result is positive or negative
        if avg_co2_savings >= 0:
            avg_co2_savings = 0
        else:
            # Increase the result by x% if slider value is > 0
            if waste_reduction_percentage > 0:
                avg_co2_savings *= (1 + waste_reduction_percentage)
            avg_co2_savings = -avg_co2_savings
        
        # Get the average revenue
        average_revenue_material = filtered_data['average_revenue_material'].iloc[0]
        
        # Check if average_revenue_material is nan, then return 0
        if pd.isna(average_revenue_material):
            avg_cost_savings = 0
        else:
            # Calculate cost savings
            avg_cost_savings = avg_waste_volume * average_revenue_material
            avg_cost_savings *= (1 + waste_reduction_percentage / 100)
        
        return avg_co2_savings, avg_cost_savings
    
    return 0, 0


# Perform query using pandas-gbq
@st.cache_data(ttl=86400, show_spinner=False)
def run_query():
    # Define the query
    query = """
    SELECT *
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.total_emissions_to_date_new`
    """
    # Read data directly into DataFrame
    return pandas_gbq.read_gbq(query, project_id = project_id, credentials=credentials)

# Read data using the cached function
material_emissions_data = run_query()

# Perform query using pandas-gbq
@st.cache_data(ttl=86400, show_spinner=False)
def run_query_forecast_data():
    # Define the query
    query = """
    SELECT material, month_year, forecast
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.forecasts_new`
    """
    # Read data directly into DataFrame
    return pandas_gbq.read_gbq(query, project_id = project_id, credentials=credentials)

# Read data using the cached function
forecasts_data = run_query_forecast_data()



def page_calculate_emission_potential():
    st.title("Calculate Your Emission Potential")
    st.subheader("Reduce emissions by sorting waste")

    st.write(" ")
    
    material_options = material_emissions_data["mapped_BE_material"].unique().tolist()
    selected_material = st.selectbox("Pick a material", material_options)

    st.write(" ")

    waste_reduction_percentage = st.slider("Pick a % of waste you want to reduce", min_value=10, max_value=100, format="%d%%", value=15)


    st.write(" ")

    if st.button("Calculate CO2 reduction potential", key="calculate_button"):
        # Filter data for selected material
        filtered_data = material_emissions_data[material_emissions_data["mapped_BE_material"] == selected_material]
        
        # Convert month_year to datetime and sort by it
        filtered_data['month_year'] = pd.to_datetime(filtered_data['month_year'])
        filtered_data = filtered_data.sort_values(by='month_year')
        
        min_emissions = filtered_data['total_emissions'].min()
        max_emissions = filtered_data['total_emissions'].max()
        
        #specific override for some materials
        if selected_material in ('BAUSCHUTT','CONSTRUCTION'):
            min_emissions = 0
        elif selected_material == 'METAL':
            min_emissions = 500

        # Plot area chart of total emissions by month_year using st.area_chart
        emissions_chart = alt.Chart(filtered_data).mark_area().encode(
            x=alt.X('month_year:T', axis=alt.Axis(labelAngle=45, format='%m/%Y', title=None)),  # Tilt x-axis labels by 45 degrees and remove label
            y=alt.Y('total_emissions:Q', title='CO2 kgs emitted', scale=alt.Scale(domain=[min_emissions, max_emissions])),  # Add y-axis label
            color=alt.value('#5D46EB'),
            tooltip=['month_year:T', 'total_emissions:Q']
        ).properties(
            width=400,  # Adjust width
            height=300  # Adjust height
        )

        # Filter forecast data for selected material
        filtered_forecast_data = forecasts_data[forecasts_data["material"] == selected_material]

        # Convert month_year to datetime and sort by it
        filtered_forecast_data['month_year'] = pd.to_datetime(filtered_forecast_data['month_year'])
        filtered_forecast_data = filtered_forecast_data.sort_values(by='month_year')
          
        reduction_percentage = waste_reduction_percentage / 100
        adjusted_forecast_data = filtered_forecast_data.copy()
        adjusted_forecast_data['forecast'] *= (1 - reduction_percentage)
        
        
                # Rename the 'forecast' column in adjusted_forecast_data to 'adjusted_forecast'
        adjusted_forecast_data.rename(columns={'forecast': 'adjusted_forecast'}, inplace=True)

        # Rename the 'forecast' column in original_forecast_data to 'original_forecast'
        filtered_forecast_data.rename(columns={'forecast': 'status_quo_forecast'}, inplace=True)

        # Combine original and adjusted forecasts
        forecast_data = pd.merge(filtered_forecast_data, adjusted_forecast_data, how='left', on=['material', 'month_year'])
        
        # Combine the data into a single dataframe with appropriate labels
        status_quo_data = forecast_data[['month_year', 'status_quo_forecast']].copy()
        status_quo_data.rename(columns={'status_quo_forecast': 'forecast'}, inplace=True)
        status_quo_data['type'] = 'Status Quo Forecast'
        adjusted_data = forecast_data[['month_year', 'adjusted_forecast']].copy()
        adjusted_data.rename(columns={'adjusted_forecast': 'forecast'}, inplace=True)
        adjusted_data['type'] = 'Adjusted Forecast'
        combined_data = pd.concat([status_quo_data, adjusted_data])
        
        # testing some new logic
        
    
        # Filter forecast data for selected material
        filtered_forecast_data = forecast_data[forecast_data["material"] == selected_material]
        filtered_forecast_data['month_year'] = pd.to_datetime(filtered_forecast_data['month_year'])
        filtered_forecast_data = filtered_forecast_data.sort_values(by='month_year')

       # Calculate the reduction per period
        reduction_percentage = waste_reduction_percentage / 100
        reduction_per_period = reduction_percentage / 6  # Distribute the reduction evenly over the first 6 periods
       
        # Apply reduction to the first 6 forecasts
        for i in range(6):
            filtered_forecast_data['adjusted_forecast'].iloc[i] *= (1 - reduction_per_period * (i + 1))

        # Apply rolling window forecast to the adjusted forecasts
        adjusted_forecasts = filtered_forecast_data.copy()
        adjusted_forecasts['adjusted_forecast'] = adjusted_forecasts['adjusted_forecast'].rolling(window=3, min_periods=1).mean()

        # Rename the 'adjusted_forecast' column in combined_data
        adjusted_forecasts.rename(columns={'adjusted_forecast': 'forecast'}, inplace=True)
        
        # Create a new DataFrame combining the original and adjusted forecasts
        status_quo_data = adjusted_forecasts[['month_year', 'status_quo_forecast']].copy()
        status_quo_data.rename(columns={'status_quo_forecast': 'forecast'}, inplace=True)
        status_quo_data['type'] = 'Status Quo Forecast'

        # Extract adjusted forecasts
        adjusted_data = adjusted_forecasts[['month_year', 'forecast']].copy()
        adjusted_data['type'] = 'Adjusted Forecast'

        # Combine the data into a single dataframe
        combined_data = pd.concat([status_quo_data, adjusted_data])
        
        
        combined_chart = alt.Chart(combined_data).mark_area().encode(
            x=alt.X('month_year:T', axis=alt.Axis(labelAngle=45, format='%m/%Y', title=None)), 
            y = alt.Y('forecast:Q', title='CO2 kgs generated forecast', stack=None, scale=alt.Scale(domain=[min_emissions, max_emissions])),
            color= alt.Color('type:N',scale=alt.Scale(domain=['Status Quo Forecast', 'Adjusted Forecast'], range=['#5D46EB', '#E6E4F2']), title='Scenarios'),
            tooltip=['month_year:T', 'forecast:Q']
        ).properties(
            width = 400,
            height = 300,
            title = 'Emissions forecast'
        )

        
         # Calculate CO2 savings
        avg_co2_savings = calculate_savings(selected_material, reduction_percentage)[0]
        avg_cost_savings = calculate_savings(selected_material, reduction_percentage)[1]
        # Create a new row layout
        
        st.altair_chart(emissions_chart | combined_chart, use_container_width=True)
        
        
        st.write(" ")

        # Assuming you have the combined_data DataFrame containing both status quo and adjusted forecast values
        status_quo_forecast_values = combined_data[combined_data['type'] == 'Status Quo Forecast']['forecast']
        adjusted_forecast_values = combined_data[combined_data['type'] == 'Adjusted Forecast']['forecast']

        # Calculate the difference between the adjusted forecast and status quo forecast
        differences = adjusted_forecast_values - status_quo_forecast_values

        # Calculate the total decrease in emissions generated
        total_decrease = differences.sum()

        # Calculate the average percentage decrease
        average_percentage_decrease = (total_decrease / status_quo_forecast_values.sum()) * 100


       
        # Display additional information
        st.markdown(
            f"<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; text-align: center;'>"
            f"<p>By reducing your <strong>{selected_material}</strong> waste by <strong>{waste_reduction_percentage}%</strong>, your emissions are projected to decrease by <strong>{-average_percentage_decrease:.2f}%</strong> on average</p>"
            "</div>",
            unsafe_allow_html=True
        )

        
        st.write(" ")
        
        
        col1, col2 = st.columns(2)


        with col1:
            st.markdown(
                        "<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        f"<h3><strong>{avg_co2_savings:.2f}</strong></h3>"
                        f"<p><strong>Projected monthly CO2 kg savings</strong></p>"
                        "<p>By recycling this material relative to incineration with energy recovery</p>"
                        "</div>", unsafe_allow_html=True)

        
        with col2:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        f"<h3><strong>{avg_cost_savings:.2f} €</strong></h3>"
                        f"<p><strong>Projected cost savings</strong></p>"
                        "<p>By recycling this material</p>"
                        "</div>", unsafe_allow_html=True)
        
        st.write(" ")


page_calculate_emission_potential()

if st.button("Next", key="next_button"):
    st.switch_page("pages/page_2.py")