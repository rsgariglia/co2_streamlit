import streamlit as st
import pandas as pd
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
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.total_emissions_to_date`
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
    SELECT *
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.forecasts`
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

    default_reduction_percentage = 0
    waste_reduction_percentage = st.slider("Pick a % of waste you want to reduce", 0, 100, (default_reduction_percentage, default_reduction_percentage))

    st.write(" ")

    if st.button("Calculate CO2 reduction potential", key="calculate_button"):
        # Filter data for selected material
        filtered_data = material_emissions_data[material_emissions_data["mapped_BE_material"] == selected_material]

        # Convert month_year to datetime and sort by it
        filtered_data['month_year'] = pd.to_datetime(filtered_data['month_year'])
        filtered_data = filtered_data.sort_values(by='month_year')

        # Plot area chart of total emissions by month_year using st.area_chart
        emissions_chart = alt.Chart(filtered_data).mark_area().encode(
            x=alt.X('month_year:T', axis=alt.Axis(labelAngle=45, format='%m/%Y', title=None)),  # Tilt x-axis labels by 45 degrees and remove label
            y=alt.Y('total_emissions:Q', title='CO2 kgs emitted'),  # Add y-axis label
            color=alt.value('blue'),
            tooltip=['month_year:T', 'total_emissions:Q']
        ).properties(
            width=400,  # Adjust width
            height=300  # Adjust height
        ).interactive()

        # Filter forecast data for selected material
        filtered_forecast_data = forecasts_data[forecasts_data["material"] == selected_material]

        # Convert month_year to datetime and sort by it
        filtered_forecast_data['month_year'] = pd.to_datetime(filtered_forecast_data['month_year'])
        filtered_forecast_data = filtered_forecast_data.sort_values(by='month_year')

        # Plot a chart for original forecast emissions
        original_forecast_chart = alt.Chart(filtered_forecast_data).mark_area().encode(
            x=alt.X('month_year:T', axis=alt.Axis(labelAngle=45, format='%m/%Y', title='Future emissions')),
            y=alt.Y('forecast:Q', title='CO2 kgs emitted'),
            color=alt.value('blue'),
            tooltip=['month_year:T', 'forecast:Q']
        ).properties(
            width=400,  # Adjust width
            height=300  # Adjust height
        ).interactive()

        # Calculate the adjusted forecast
        reduction_percentage = waste_reduction_percentage[1] / 100
        adjusted_forecast_data = filtered_forecast_data.copy()
        adjusted_forecast_data['forecast'] *= (1 - reduction_percentage)

        # Plot an overlay of adjusted forecast on the same chart
        adjusted_forecast_chart = alt.Chart(adjusted_forecast_data).mark_area().encode(
            x=alt.X('month_year:T', axis=alt.Axis(labelAngle=45, format='%m/%Y', title='Future emissions')),
            y=alt.Y('forecast:Q', title='Adjusted CO2 kgs emitted'),
            color=alt.value('red'),
            tooltip=['month_year:T', 'forecast:Q']
        ).interactive()

        # Display both original and adjusted forecasts on the same chart
        combined_chart = (original_forecast_chart + adjusted_forecast_chart).properties(
            width=400,  # Adjust width
            height=300,  # Adjust height
            title="Emissions Forecast"
        )

        # Add legend
        combined_chart = combined_chart.properties(
            title="Emissions Forecast",
            width=400,
            height=300
        ).interactive()
        
         # Calculate CO2 savings
        avg_co2_savings = calculate_savings(selected_material, reduction_percentage)[0]
        avg_cost_savings = calculate_savings(selected_material, reduction_percentage)[1]
        # Create a new row layout
        
        st.altair_chart(emissions_chart | combined_chart, use_container_width=True)
        
        # Add a space between the charts and the average CO2 savings box
        st.write(" ")
        
        # Create two columns layout for the boxes
        col1, col2 = st.columns(2)

        # Display the average CO2 savings box in the first column
        with col1:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<h3>Projected monthly CO2 kg savings</h3>"
                        "<p>By recycling relative to incineration with energy recovery</p>"
                        f"<p>{avg_co2_savings}</p>"
                        "</div>", unsafe_allow_html=True)

        # Display the cost savings box in the second column
        with col2:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<h3>Cost savings</h3>"
                        "<p>Relative to incineration with energy recovery</p>"
                        f"<p>{avg_cost_savings}</p>"
                        "</div>", unsafe_allow_html=True)
        
        st.write(" ")

# Display the content of Page 1 on the Home page
page_calculate_emission_potential()

if st.button("Next", key="next_button"):
    st.switch_page("pages/page_2.py")