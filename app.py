import streamlit as st
import pandas as pd
import altair as alt
from st_pages import Page, show_pages
import pandas_gbq


# Set Streamlit theme to light
st.set_page_config(layout="wide", page_title="Emissions App", initial_sidebar_state="expanded")

# Define BigQuery credentials
credentials = st.secrets["gcp_service_account"]
project_id = credentials["project_id"]

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#specifying sidebar layout
show_pages(
    [
        Page("app.py", "Your estimated emissions"),
        Page("pages/page_1.py", "Calculate your reduction potential"),
        Page("pages/page_2.py", "Identify ways to reduce emissions"),
        Page("pages/page_3.py", "Detailed CO2 report")
    ]
)

# Perform query using pandas-gbq
@st.cache_resource(ttl=86400, show_spinner=False)
def run_query():
    # Define the query
    query = """
    SELECT material, emissions_generated
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.emissions_generated`
    """
    # Read data directly into DataFrame
    return pandas_gbq.read_gbq(query, project_id=project_id)

# Read data using the cached function
emissions_data = run_query()


def page_your_estimated_emissions():
    st.title("Your Estimated Emissions")
    st.markdown("This page displays your estimated emissions. <span style='text-decoration: underline; cursor: help;' title='placeholder for more info'>Learn more</span>", unsafe_allow_html=True)


    # Select first 7 results
    emissions_data_first_7 = emissions_data.head(7)

    # Plot bar chart of emissions generated using Altair
    chart = alt.Chart(emissions_data_first_7).mark_bar().encode(
        x=alt.X('material:N', sort=None, axis=alt.Axis(labelAngle=45)),  # Disabling sorting and tilting labels
        y='emissions_generated:Q'  # Quantitative field
    ).properties(
        width=600,
        height=300  # Adjust height
    )
    st.altair_chart(chart, use_container_width=True)

# Display the content of Page 1 on the Home page
page_your_estimated_emissions()

# Add navigation buttons at the bottom right
if st.button("Next", key="next_button"):
    st.switch_page("pages/page_1.py")