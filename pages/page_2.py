import streamlit as st
import json
from streamlit_lottie import st_lottie


st.set_page_config(layout="wide", page_title="Emissions App", initial_sidebar_state="expanded")

# reading in lottie files

#with open('Illustration-Go-circular.json', 'r') as f:
    #circular = json.load(f)
#st_lottie(circular, width=200, height=200)

with open('Illustration-Sorting-optimised.json', 'r') as f:
    sort = json.load(f)
st_lottie(sort, width=200, height=200)

with open('Illustration-ReducePickups-optimised.json', 'r') as f:
    pickup = json.load(f)
st_lottie(pickup, width=200, height=200)

with open('Illustration-Transport-emissions-optimised.json', 'r') as f:
    transport = json.load(f)
st_lottie(transport, width=200, height=200)

with open('Illustration-Go-circular_new.json', 'r') as f:
    circular = json.load(f)
st_lottie(circular, width=200, height=200)

def page_identify_ways_to_reduce_emissions():
    st.title("Identify Ways to Reduce Emissions")
    st.write("This page helps you identify ways to reduce emissions.")

    st.write("")
    st.markdown("""
    <style>

        .stTabs [data-baseweb="tab-list"] {
            gap: 4px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #F0F2F6;
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
            padding-left: 5px;
            padding-right: 5px;
            border: solid;
        }

        .stTabs [aria-selected="true"] {
            background-color: #d3d3d3;
            border-color: blue;
        }
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: pink;
        }

    </style>""", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Go Circular", "Optimise transport emissions", "Reduce pickups", "Avoid incineration through sorting"])

    with tab1:
        st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                    "<h3>Take back your materials</h3>"
                    "<p>You are managing <b>0</b> circular waste streams in Resourcify</p>"
                    "<a href='https://www.google.com' target='_blank'><button>Explore takeback opportunities</button></a>"
                    "</div>", unsafe_allow_html=True)
        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<h3>123,456 t of CO2 saved</h3>"
                        "<p>through take-back by other Resourcify customers</p>"
                        "</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(
                        "<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<h3>Box 2.1</h3>"
                        "<p>The Lottie icon will have to go here</p>"
                        "</div>",
                        unsafe_allow_html=True)

        st.write("")
       

    with tab2:
        st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; display: flex; justify-content: space-between;'>"
            "<div>"
            "<h4><b>0</b> of your recyclers have fed back transport emission data</h4>"
            "<p>Our best-guess estimate is that your CO2 emissions per pickup are 123.45 kg.</p>"
            "</div>"
            "<div style='align-self: center;'>"
            "<a href='https://www.google.com' target='_blank'>"
            "<button>Ask recyclers to fill in emissions data</button>"
            "</a>"
            "</div>"
            "</div>", unsafe_allow_html=True)

        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
            "<h4>You are 7% closer to your recycler than the average Resourcify user</h4>"
            "<p style='margin: 0;'>Average transport distance</p>"
            "<p><b>34.7 km</b></p>"
            "</div>", unsafe_allow_html=True)


        with col2:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<h3>Box 2.2</h3>"
                        "<p>Content for Box 2.3</p>"
                        "</div>", unsafe_allow_html=True)
        st.write("")

    with tab3:
        st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; display: flex; justify-content: space-between;'>"
            "<div>"
            "<h4>Up to 31% of your pick-ups might be avoidable, avoiding up to 450t of CO2 emissions</h4>"
            "<p style='margin: 0;'>We estimate fill levels based on weight distribution per container.</p>"
            "<p>We didn't find any bales and presses in your container types so we assume that you are not compressing your waste.</p>"
            "</div>"
            "<div style='align-self: center;'>"
            "<a href='https://www.google.com' target='_blank'>"
            "<button>Learn more about bales and presses</button>"
            "</a>"
            "</div>"
            "</div>", unsafe_allow_html=True)
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; max-width: 450px; margin-right: 2px;'>"
                "<h4>Your pickup count</h4>"
                "<p style='margin: 0;'><b>10,205</b></p>"
                "<p>Total pickups last 12 months</p>"
                "<p style='margin: 0;'><b>133</b></p>"
                "<p>Average pickup per location</p>"
                "<p style='margin: 0;'><b>14%</b></p>"
                "<p>Interval pickups</p>"
                "</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; max-width: 450px; margin-right: 2px;'>"
                "<h4>Your container fill levels</h4>"
                "<p style='margin: 0;'><b>23%</b></p>"
                "<p>Containers with no waste volume</p>"
                "<p style='margin: 0;'><b>75%</b></p>"
                "<p>Target container fill levels</p>"
                "<p style='margin: 0;'><b>31%</b></p>"
                "<p>Estimated waste volume missing</p>"
                "</div>", unsafe_allow_html=True)
            
        with col3:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; width: 100%;'>"
                        "<h3>Box 2.3</h3>"
                        "<p>Content for Box 2.3</p>"
                        "</div>", unsafe_allow_html=True)
            
        
        
        st.write("")

    with tab4:
        st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px; display: flex; justify-content: space-between;'>"
            "<div>"
            "<h4>You are collecting 11 materials on average</h4>"
            "<p style='margin: 0;'>On average Resourcify users have 27 materials.</p>"
            "<p>Depending on your available space, there might be room for more granular sorting</p>"
            "</div>"
            "<div style='align-self: center;'>"
            "<a href='https://www.google.com' target='_blank'>"
            "<button>Order new container</button>"
            "</a>"
            "</div>"
            "</div>", unsafe_allow_html=True)
        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<p style='margin: 0;'><b>15%</b></p>"
                        "<p>of your waste is mixed waste being incinerated</p>"
                        "<p style='margin: 0;'><b>Up to 580kg of extra CO2</b></p>"
                        "<p>is emitted for every ton of waste incinerated and not recycled</p>"
                        "</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div style='border: 1px solid #D3D3D3; padding: 10px; border-radius: 5px;'>"
                        "<h3>Box 2.4</h3>"
                        "<p>Content for Box 2.4</p>"
                        "</div>", unsafe_allow_html=True)
        st.write("")

page_identify_ways_to_reduce_emissions()

if st.button("Next", key="next_button"):
    st.switch_page("pages/page_3.py")
