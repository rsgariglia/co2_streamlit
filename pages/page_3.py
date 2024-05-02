import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Emissions App", initial_sidebar_state="expanded")

st.markdown('<style> '+ open('./style.css').read()+' </style>', unsafe_allow_html=True)

def page_a_deeper_look():
    st.title("A deeper look into your CO2 savings")
    st.write("Break down of your most emitting materials by location")

    st.write("")
    
    # Empty table with one header and a row
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True, help='CO2 savings are calculated by comparing recycling to the next best recycling path for a material')
    st.write("### <i class='fa fa-trash'></i> Residual waste", unsafe_allow_html=True)
    empty_table_1 = pd.DataFrame(columns=["Material type", "Quantity (tonnes)", "kgs CO2 saved", 'kgs CO2 avoided'])
    
    # Adding the first row
    dictionary_1 = {"Material type": "Residual waste", 
                    "Quantity (tonnes)": 32.53, 
                    "kgs CO2 saved": 12426.57, 
                    "kgs CO2 avoided": 7481.62}
    
    empty_table_1.loc[0] = dictionary_1
    
    st.dataframe(empty_table_1, hide_index=True, width=900)  # Adjust the width as needed

    st.write("")
    st.write("")

    # Empty table with one header and a row
    st.write("### Location")
    empty_table_2 = pd.DataFrame(columns=["Location: city - postcode", "Material type", "Quantity (tonnes)", "kgs CO2 saved", 'kgs CO2 avoided'])
    
    # Adding the rows with specified locations and random values for other columns
    locations = ["Berlin - 10711", "Hamburg - 22525", "Laatzen - 30880", "Leipzig - 04356", "Mannheim-68161"]
    materials = ["Abfall zur Verwertung", "gemischte Verpackungen", "Altreifen", "Spraydosen", "gemischter Bauabfall"]
    quantities = [15, 20, 25, 30, 35]
    
    total_quantity = empty_table_1.iloc[0]["Quantity (tonnes)"]
    total_co2_saved = empty_table_1.iloc[0]["kgs CO2 saved"]
    total_co2_avoided = empty_table_1.iloc[0]["kgs CO2 avoided"]
    
    for i, location in enumerate(locations):
        quantity = (quantities[i] / sum(quantities)) * total_quantity
        co2_saved = np.random.uniform(0, total_co2_saved / len(locations))  # Random value within range
        co2_avoided = np.random.uniform(0, total_co2_avoided / len(locations))
        
        dictionary_2 = {"Location: city - postcode": location,
                        "Material type": materials[i],
                        "Quantity (tonnes)": quantity,
                        "kgs CO2 saved": co2_saved,
                        "kgs CO2 avoided": co2_avoided}
        empty_table_2.loc[i] = dictionary_2
    
    st.dataframe(empty_table_2, hide_index=True, width=900)
    
    st.write("")
    st.write("-----------------------------")
    st.write("")
    
    # Empty table with one header and a row
    #st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    st.write("### <i class='fa fa-laptop'></i> Electronic waste", unsafe_allow_html=True)  # Add icon of a laptop

    empty_table_1 = pd.DataFrame(columns=["Material type", "Quantity (tonnes)", "kgs CO2 saved", 'kgs CO2 avoided'])
    
    # Adding the first row
    dictionary_1 = {"Material type": "Electronic waste", 
                    "Quantity (tonnes)": 25.6, 
                    "kgs CO2 saved": 11106.2, 
                    "kgs CO2 avoided": 6043.3}
    
    empty_table_1.loc[0] = dictionary_1
    
    st.dataframe(empty_table_1, hide_index=True, width=900)  # Adjust the width as needed

    st.write("")
    st.write("")

    # Empty table with one header and a row
    st.write("### Location")
    empty_table_2 = pd.DataFrame(columns=["Location: city - postcode", "Material type", "Quantity (tonnes)", "kgs CO2 saved", 'kgs CO2 avoided'])
    
    # Adding the rows with specified locations and random values for other columns
    locations = ["Munich - 80687", "Dortmund- 44147", "Wittmund- 26409", "Waren - 04356", "Heilbronn-74078"]
    materials = ["Starter-Batterien", "Elektronikschrott gemischt", "Energiesparlampen / LEDs", "Monitore", "Alkalibatterien"]
    quantities = [15, 20, 25, 30, 35]
    
    total_quantity = empty_table_1.iloc[0]["Quantity (tonnes)"]
    total_co2_saved = empty_table_1.iloc[0]["kgs CO2 saved"]
    total_co2_avoided = empty_table_1.iloc[0]["kgs CO2 avoided"]
    
    for i, location in enumerate(locations):
        quantity = (quantities[i] / sum(quantities)) * total_quantity
        co2_saved = np.random.uniform(0, total_co2_saved / len(locations))  # Random value within range
        co2_avoided = np.random.uniform(0, total_co2_avoided / len(locations))
        
        dictionary_2 = {"Location: city - postcode": location,
                        "Material type": materials[i],
                        "Quantity (tonnes)": quantity,
                        "kgs CO2 saved": co2_saved,
                        "kgs CO2 avoided": co2_avoided}
        empty_table_2.loc[i] = dictionary_2
    
    st.dataframe(empty_table_2, hide_index=True, width=900)
    
    st.write("")
    st.write("-----------------------------")
    st.write("")

    #st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    st.write("### <i class='fas fa-book'></i> Paper waste", unsafe_allow_html=True)
    empty_table_1 = pd.DataFrame(columns=["Material type", "Quantity (tonnes)", "kgs CO2 saved", 'kgs CO2 avoided'])
    
    # Adding the first row
    dictionary_1 = {"Material type": "Paper waste", 
                    "Quantity (tonnes)": 10.15, 
                    "kgs CO2 saved": 2240.3, 
                    "kgs CO2 avoided": 1578.4}
    
    empty_table_1.loc[0] = dictionary_1
    
    st.dataframe(empty_table_1, hide_index=True, width=900)  # Adjust the width as needed

    st.write("")
    st.write("")

    # Empty table with one header and a row
    st.write("### Location")
    empty_table_2 = pd.DataFrame(columns=["Location: city - postcode", "Material type", "Quantity (tonnes)", "kgs CO2 saved", 'kgs CO2 avoided'])
    
    # Adding the rows with specified locations and random values for other columns
    locations = ["Bonn - 10812", "Bremen - 24672", "Dresden- 32890", "Karlsruhe - 01231", "Stuttgart-68165"]
    materials = ["Papier, Pappe, Karton", "Mischpapier (B12)", "Aktenvernichtung", "Altpapier", "Kaufhausaltpapier"]
    quantities = [15, 20, 25, 30, 35]
    
    total_quantity = empty_table_1.iloc[0]["Quantity (tonnes)"]
    total_co2_saved = empty_table_1.iloc[0]["kgs CO2 saved"]
    total_co2_avoided = empty_table_1.iloc[0]["kgs CO2 avoided"]
    
    for i, location in enumerate(locations):
        quantity = (quantities[i] / sum(quantities)) * total_quantity
        co2_saved = np.random.uniform(0, total_co2_saved / len(locations))  # Random value within range
        co2_avoided = np.random.uniform(0, total_co2_avoided / len(locations))
        
        dictionary_2 = {"Location: city - postcode": location,
                        "Material type": materials[i],
                        "Quantity (tonnes)": quantity,
                        "kgs CO2 saved": co2_saved,
                        "kgs CO2 avoided": co2_avoided}
        empty_table_2.loc[i] = dictionary_2
    
    st.dataframe(empty_table_2, hide_index=True, width=900)
# Call the function
page_a_deeper_look()


if st.button("Back", key="next_button"):
    st.switch_page("app.py")

