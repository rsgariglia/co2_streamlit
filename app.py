import streamlit as st
import pandas as pd
import altair as alt
from st_pages import Page, show_pages
import pandas_gbq
from google.oauth2 import service_account
from google.cloud import bigquery



# Set Streamlit theme to light
st.set_page_config(layout="wide", page_title="Emissions App", initial_sidebar_state="expanded")

# Define BigQuery credentials
#credentials = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(credentials=credentials)
#project_id = credentials["project_id"]
project_id = st.secrets["gcp_service_account"]["project_id"]

st.markdown('<style> '+ open('./style.css').read()+' </style>', unsafe_allow_html=True)
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
        Page("app.py", "Your estimated emissions", icon='⭕'),
        Page("pages/page_1.py", "Calculate your reduction potential", icon='⭕'),
        Page("pages/page_2.py", "Identify ways to reduce emissions", icon='⭕'),
        Page("pages/page_3.py", "Detailed CO2 report", icon='⭕')
    ]
)


# Perform query using pandas-gbq
@st.cache_data(ttl=86400, show_spinner=False)
def run_query():
    # Define the query
    query = """
    SELECT material, emissions_generated
    FROM `analytics-data-platform-395911.streamlit_app_IFAT.emissions_generated`
    """
    # Read data directly into DataFrame
    return pandas_gbq.read_gbq(query, project_id = project_id, credentials=credentials)

# Read data using the cached function
emissions_data = run_query()


def page_your_estimated_emissions():
    pageTitleText = """
            <div class="page-title-container">
                <div class="title">
                    <span class="inline-block-span">Learn how to <i class="italicised-text">reduce your</i></span>
                    <span class="inline-block-span"><i class="italicised-text">C0<sub>2</sub> emissions</i></span>
                </div>
                <div class="callout">
                    <span class="inline-block-span">Status quo: Your estimated C02</span> 
                    <span class="inline-block-span">emissions over the last 12 months </span>
                </div>
                <div class="muted-text">
                    <span class="inline-block-span">
                        This data is calculated based on your material quantities and certified average
                    </span>
                    <span class="inline-block-span">  
                        emission values per recyclingpath. <a href="" target="_blank">Learn more</a>
                    </span>
                </div>
            </div>
            """
    
    st.markdown(pageTitleText, unsafe_allow_html=True)


    # Select first 7 results
    emissions_data_first_7 = emissions_data.head(7)

    # Plot bar chart of emissions generated using Altair
    chart = alt.Chart(emissions_data_first_7).mark_bar().encode(
        x=alt.X('material:N', sort=None, axis=alt.Axis(labelAngle=45)),
        y = alt.Y('emissions_generated:Q', title='Emissions generated'),
        color=alt.value('#5D46EB')
    ).properties(
        width=600,
        height=300  # Adjust height
    )
    st.altair_chart(chart, use_container_width=True)

# Display the content of Page 1 on the Home page
page_your_estimated_emissions()

# Add navigation buttons at the bottom right
if st.button("Continue", key="next_button", type="primary"):
    st.switch_page("pages/page_1.py")
    

y = alt.Y('forecast:Q', title='CO2 kgs generated forecast')