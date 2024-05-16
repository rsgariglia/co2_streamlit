import streamlit as st
import json
from streamlit_lottie import st_lottie


st.set_page_config(layout="wide", page_title="Emissions App", initial_sidebar_state="expanded")
st.markdown('<style> '+ open('./style.css').read()+' </style>', unsafe_allow_html=True)

# reading in lottie files

#with open('Illustration-Go-circular.json', 'r') as f:
    #circular = json.load(f)
#st_lottie(circular, width=200, height=200)


#icon_gc = st.image("GoCircular-Icon1.svg", width=30)


def page_identify_ways_to_reduce_emissions():
    pageTitleTxt = """
                    <div class="page-title-container page1-page-container-top">
                        <div class="header-text">
                            <span class="inline-block-span">Identify ways to <i class="purple-color-text">reduce your CO2 emissions</i></span>
                        </div>
                    <div>
                """
    st.markdown(pageTitleTxt, unsafe_allow_html=True)
    st.write("")

    #tab1_icon = f'{icon_gc.markdown("")} '
    tab1, tab2, tab3, tab4 = st.tabs(['Go Circular', "Optimise transport emissions", "Reduce pickups", "Avoid incineration through sorting"])

    with tab1:
        st.markdown("""
                    <div class="tab-callout-container">
                        <div class="title">0 circular waste streams</div>
                        <div class="text sub-header-text">You are not yet managing circular waste streams in Resourcify</div>
                        <a class="link-btn-primary" href='https://circularity.demo.enterprise.resourcify.de/circular-future' target='_blank'>
                            Explore take-back opportunities
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                """
                    <div class="tab-mini-callout">
                        <div class="icon">
                            <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                <path d="M28.3971 34.4064V27.0169C28.5603 27.0441 28.7256 27.0583 28.8912 27.0595C29.4983 27.0477 30.0974 26.9235 30.6559 26.6938C32.0732 26.1127 33.3546 25.2625 34.4235 24.1938C36.9294 21.7619 37 18.0119 37 17.8503C37 17.6248 36.907 17.4085 36.7416 17.2491C36.5761 17.0896 36.3517 17 36.1177 17C35.95 17 32.0589 17.068 29.5442 19.5C28.1265 20.7591 27.1104 22.3813 26.6148 24.1768C26.2821 23.7482 25.9195 23.342 25.5295 22.9608C23.9688 21.6318 21.9732 20.8734 19.8913 20.818C19.7731 20.8114 19.6548 20.8301 19.545 20.8727C19.4352 20.9154 19.3365 20.9809 19.256 21.0646C19.1731 21.1451 19.1078 21.2407 19.0639 21.3458C19.02 21.451 18.9983 21.5635 19.0001 21.6768C19.0572 23.6792 19.8409 25.5989 21.2148 27.102C22.6707 28.505 24.5148 29.5594 25.9618 29.5594C26.1893 29.5566 26.4151 29.5222 26.6324 29.4574V34.4489C24.2513 34.6735 21.9891 35.5598 20.1207 36.9999C20.0183 37.0652 19.9312 37.1505 19.8649 37.2502C19.7987 37.3498 19.7547 37.4618 19.7359 37.5787C19.7172 37.6957 19.7239 37.8152 19.7558 37.9295C19.7877 38.0438 19.844 38.1505 19.9211 38.2426C19.9982 38.3348 20.0944 38.4104 20.2036 38.4646C20.3128 38.5189 20.4325 38.5505 20.5551 38.5576C20.6777 38.5647 20.8005 38.547 20.9156 38.5058C21.0307 38.4645 21.1356 38.4005 21.2236 38.3179C23.1305 36.8556 25.4994 36.0665 27.9362 36.082C30.3731 36.0975 32.731 36.9165 34.6177 38.4029C34.7068 38.4745 34.8098 38.5285 34.9206 38.5617C35.0314 38.5949 35.1479 38.6067 35.2635 38.5964C35.3791 38.5861 35.4914 38.554 35.5941 38.5018C35.6967 38.4497 35.7877 38.3785 35.8618 38.2924C35.9361 38.2065 35.992 38.1073 36.0265 38.0004C36.0609 37.8936 36.0732 37.7813 36.0625 37.67C36.0519 37.5586 36.0185 37.4503 35.9644 37.3514C35.9103 37.2525 35.8364 37.1648 35.7471 37.0934C33.6661 35.4503 31.0853 34.5068 28.3971 34.4064ZM30.7794 20.6905C31.9946 19.6387 33.5166 18.9735 35.1382 18.7857C34.9433 20.3485 34.2532 21.8153 33.1618 22.9864C32.2642 23.8922 31.1871 24.6151 29.9942 25.1122C29.1648 25.4268 28.6089 25.3928 28.4412 25.2397C28.4412 25.2397 28.4412 25.1717 28.3971 25.1462V24.8571C28.3931 24.7589 28.3753 24.6616 28.3442 24.568C28.7341 23.0694 29.5826 21.7184 30.7794 20.6905ZM26.2354 27.7993C25.9971 28.0203 24.3471 27.7142 22.4677 25.903C21.6083 24.9864 21.0523 23.8436 20.8707 22.6207C22.1377 22.7933 23.3215 23.3296 24.2677 24.1598C26.1471 25.971 26.4648 27.5612 26.2354 27.7993Z" fill="#264B4B"/>
                            </svg>
                        </div>
                        <div class="text-wrapper">
                            <div class="header">
                                100.5 t
                            </div>
                            <div class="text">
                                <span class="inline-block-span">
                                    CO2 saved through take-back by other
                                </span>
                                <span class="inline-block-span">
                                    Resourcify customers
                                </span>
                            </div>
                        </div>
                    </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                    <div class="multi-item-callout illustration-container">
                        <div class="item tab-mini-callout">
                            <div class="illustration">
                                <img src="app/static/Illustration-Go-circular.gif" alt="Go Circular" />
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="text-wrapper">
                                <div class="header">
                                    Analyse your product for CO2 saving potential
                                </div>
                                <div class="text">
                                    A lifecycle analysis can help evaluate your material streams and their emissions.
                                    Whether you can save emissions through take-back depends on many factors like weight and transport.
                                    Our circularity team can calculate the business case for you.
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )

        st.write("")
       

    with tab2:
        st.markdown(
                """
                    <div class="tab-callout-container">
                        <div class="title">0 of your recyclers have fed back transport emission data</div>
                        <div class="text sub-header-text">Our best-guess estimate is that your CO2 emissions per pickup are 123,45 kg.</div>
                        <a class="link-btn-primary" href='https://circularity.demo.enterprise.resourcify.de/circular-future' target='_blank'>
                            Ask recyclers to fill in emissions data
                        </a>
                    </div>
                """,
                unsafe_allow_html=True)

        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                """
                    <div class="multi-item-callout">
                        <div class="item tab-mini-callout">
                            <div class="icon">
                                <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M31 26.5C31 28.1569 29.6569 29.5 28 29.5C26.3431 29.5 25 28.1569 25 26.5C25 24.8431 26.3431 23.5 28 23.5C29.6569 23.5 31 24.8431 31 26.5Z" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M35.5 26.5C35.5 33.6421 28 37.75 28 37.75C28 37.75 20.5 33.6421 20.5 26.5C20.5 22.3579 23.8579 19 28 19C32.1421 19 35.5 22.3579 35.5 26.5Z" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    7% closer
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        to your recycler than the average Resourcify
                                    </span>
                                    <span class="inline-block-span">
                                        customer
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                               <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M24.25 34.75C24.25 35.5784 23.5784 36.25 22.75 36.25C21.9216 36.25 21.25 35.5784 21.25 34.75M24.25 34.75C24.25 33.9216 23.5784 33.25 22.75 33.25C21.9216 33.25 21.25 33.9216 21.25 34.75M24.25 34.75H30.25M21.25 34.75H19.375C18.7537 34.75 18.25 34.2463 18.25 33.625V30.2504M35.5 34.75C35.5 35.5784 34.8284 36.25 34 36.25C33.1716 36.25 32.5 35.5784 32.5 34.75M35.5 34.75C35.5 33.9216 34.8284 33.25 34 33.25C33.1716 33.25 32.5 33.9216 32.5 34.75M35.5 34.75L36.625 34.75C37.2463 34.75 37.7537 34.2457 37.7154 33.6256C37.5054 30.218 36.3473 27.0669 34.5016 24.4328C34.1394 23.9159 33.5529 23.6077 32.9227 23.5732H30.25M32.5 34.75H30.25M30.25 23.5732V22.6148C30.25 22.0473 29.8275 21.5672 29.263 21.5086C27.6153 21.3376 25.9429 21.25 24.25 21.25C22.5571 21.25 20.8847 21.3376 19.237 21.5086C18.6725 21.5672 18.25 22.0473 18.25 22.6148V30.2504M30.25 23.5732V30.2504M30.25 34.75V30.2504M30.25 30.2504H18.25" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    34.7 km
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Average distance to recycler of other Resourcify
                                    </span>
                                    <span class="inline-block-span">
                                        customers
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )



        with col2:
            st.markdown(
                """
                    <div class="multi-item-callout illustration-container">
                        <div class="item tab-mini-callout">
                            <div class="illustration">
                                <img src="app/static/Illustration-Transport-emissions.gif" alt="Go Circular" />
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="text-wrapper">
                                <div class="header">
                                    Your recycler can influence transport emissions
                                </div>
                                <div class="text">
                                    There are recyclers with climate-neutral transportation.
                                    Call your recycler to learn more about their stance on emissions.
                                    Independently of your recycler, you can compensate for the transport emissions your waste is causing.
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )
        st.write("")

    with tab3:
        st.markdown(
                """
                    <div class="tab-callout-container">
                        <div class="title">Up to 31% of your pick-ups might be avoidable, avoiding up to 450t of C02 emissions</div>
                        <div class="text sub-header-text">
                            We estimate fill levels based on weight distributions per container.
                            <span class="inline-block-span">
                                We didn't find any bales and presses in your container types so we assume that you are not compressing your waste.
                            </span>
                        </div>
                        <a class="link-btn-primary" href='https://circularity.demo.enterprise.resourcify.de/circular-future' target='_blank'>
                            Learn more about bales and presses
                        </a>
                    </div>
                """,
                unsafe_allow_html=True)
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(
                """
                    <div class="multi-item-callout">
                        <div class="section-header">
                            Your pickup count
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                                <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M24.25 34.75C24.25 35.5784 23.5784 36.25 22.75 36.25C21.9216 36.25 21.25 35.5784 21.25 34.75M24.25 34.75C24.25 33.9216 23.5784 33.25 22.75 33.25C21.9216 33.25 21.25 33.9216 21.25 34.75M24.25 34.75H30.25M21.25 34.75H19.375C18.7537 34.75 18.25 34.2463 18.25 33.625V30.2504M35.5 34.75C35.5 35.5784 34.8284 36.25 34 36.25C33.1716 36.25 32.5 35.5784 32.5 34.75M35.5 34.75C35.5 33.9216 34.8284 33.25 34 33.25C33.1716 33.25 32.5 33.9216 32.5 34.75M35.5 34.75L36.625 34.75C37.2463 34.75 37.7537 34.2457 37.7154 33.6256C37.5054 30.218 36.3473 27.0669 34.5016 24.4328C34.1394 23.9159 33.5529 23.6077 32.9227 23.5732H30.25M32.5 34.75H30.25M30.25 23.5732V22.6148C30.25 22.0473 29.8275 21.5672 29.263 21.5086C27.6153 21.3376 25.9429 21.25 24.25 21.25C22.5571 21.25 20.8847 21.3376 19.237 21.5086C18.6725 21.5672 18.25 22.0473 18.25 22.6148V30.2504M30.25 23.5732V30.2504M30.25 34.75V30.2504M30.25 30.2504H18.25" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    10,205
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Total pickups last 12
                                    </span>
                                    <span class="inline-block-span">
                                        months
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                               <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M18.25 37H37.75M19.75 19V37M30.25 19V37M36.25 23.5V37M22.75 22.75H23.5M22.75 25.75H23.5M22.75 28.75H23.5M26.5 22.75H27.25M26.5 25.75H27.25M26.5 28.75H27.25M22.75 37V33.625C22.75 33.0037 23.2537 32.5 23.875 32.5H26.125C26.7463 32.5 27.25 33.0037 27.25 33.625V37M19 19H31M30.25 23.5H37M33.25 27.25H33.2575V27.2575H33.25V27.25ZM33.25 30.25H33.2575V30.2575H33.25V30.25ZM33.25 33.25H33.2575V33.2575H33.25V33.25Z" stroke="#0D2F2F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    133
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Average pickup count per location
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                               <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M32.0228 25.3484H37.0154V25.3466M18.9841 35.6444V30.6517M18.9841 30.6517L23.9768 30.6517M18.9841 30.6517L22.165 33.8347C23.1555 34.8271 24.4126 35.58 25.8644 35.969C30.2654 37.1483 34.7892 34.5364 35.9685 30.1353M20.0307 25.8648C21.21 21.4637 25.7338 18.8519 30.1349 20.0312C31.5866 20.4202 32.8437 21.1731 33.8342 22.1655L37.0154 25.3466M37.0154 20.3558V25.3466" stroke="#0D2F2F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    14 %
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Interval pickups
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )
            
        with col2:
            st.markdown(
                """
                    <div class="multi-item-callout">
                        <div class="section-header">
                            Your container fill levels
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                                <svg width="57" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect x="0.333374" width="56" height="56" rx="8" fill="#E6E4F2"/>
                                    <path d="M26.2123 23.5188C27.3839 22.4937 29.2833 22.4937 30.4549 23.5188C31.6265 24.544 31.6265 26.206 30.4549 27.2312C30.251 27.4096 30.025 27.5569 29.7847 27.6733C29.039 28.0341 28.3336 28.6716 28.3336 29.5V30.25M37.3334 28C37.3334 32.9706 33.3039 37 28.3334 37C23.3628 37 19.3334 32.9706 19.3334 28C19.3334 23.0294 23.3628 19 28.3334 19C33.3039 19 37.3334 23.0294 37.3334 28ZM28.3334 33.25H28.3409V33.2575H28.3334V33.25Z" stroke="#5D46EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    23%
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Containers with no waste
                                    </span>
                                    <span class="inline-block-span">
                                        volume
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                               <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect x="0.333374" width="56" height="56" rx="8" fill="#E6E4F2"/>
                                    <path d="M19.3334 29.125C19.3334 28.5037 19.8371 28 20.4584 28H22.7084C23.3297 28 23.8334 28.5037 23.8334 29.125V35.875C23.8334 36.4963 23.3297 37 22.7084 37H20.4584C19.8371 37 19.3334 36.4963 19.3334 35.875V29.125Z" stroke="#5D46EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M26.0834 24.625C26.0834 24.0037 26.5871 23.5 27.2084 23.5H29.4584C30.0797 23.5 30.5834 24.0037 30.5834 24.625V35.875C30.5834 36.4963 30.0797 37 29.4584 37H27.2084C26.5871 37 26.0834 36.4963 26.0834 35.875V24.625Z" stroke="#5D46EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M32.8334 20.125C32.8334 19.5037 33.3371 19 33.9584 19H36.2084C36.8297 19 37.3334 19.5037 37.3334 20.125V35.875C37.3334 36.4963 36.8297 37 36.2084 37H33.9584C33.3371 37 32.8334 36.4963 32.8334 35.875V20.125Z" stroke="#5D46EB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    75%
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Target container fill
                                    </span>
                                    <span class="inline-block-span">
                                        levels
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                               <svg width="53" height="52" viewBox="0 0 53 52" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect x="0.333374" width="52" height="52" rx="8" fill="#E6E4F2"/>
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M26.3334 18C26.7476 18 27.0834 18.3358 27.0834 18.75V19.0084C28.5643 19.0414 30.0215 19.172 31.4488 19.3942C32.2255 19.5151 32.9934 19.6631 33.7513 19.8372C34.155 19.9299 34.4071 20.3324 34.3144 20.7361C34.2216 21.1398 33.8192 21.3919 33.4155 21.2991C33.0502 21.2152 32.6824 21.1376 32.3124 21.0665L34.0148 28.6123C34.0899 28.9452 33.9308 29.2868 33.6277 29.4435C32.9398 29.7994 32.1589 30 31.3334 30C30.5079 30 29.7271 29.7994 29.0391 29.4435C28.736 29.2868 28.5769 28.9452 28.652 28.6123L30.423 20.763C29.3267 20.6209 28.2125 20.5351 27.0834 20.5087V32.0138C28.3779 32.0616 29.6416 32.2324 30.8629 32.5153C31.2665 32.6087 31.5178 33.0116 31.4244 33.4151C31.331 33.8187 30.9281 34.07 30.5245 33.9766C29.1786 33.6649 27.7757 33.5 26.3334 33.5C24.8911 33.5 23.4882 33.6649 22.1423 33.9766C21.7388 34.07 21.3359 33.8187 21.2424 33.4151C21.149 33.0116 21.4004 32.6087 21.8039 32.5153C23.0252 32.2324 24.2889 32.0616 25.5834 32.0138V20.5087C24.4543 20.5351 23.3402 20.6209 22.2439 20.763L24.0148 28.6123C24.0899 28.9452 23.9308 29.2868 23.6277 29.4435C22.9398 29.7994 22.1589 30 21.3334 30C20.5079 30 19.7271 29.7994 19.0391 29.4435C18.736 29.2868 18.5769 28.9452 18.652 28.6123L20.3545 21.0665C19.9844 21.1376 19.6166 21.2152 19.2513 21.2991C18.8476 21.3919 18.4452 21.1398 18.3525 20.7361C18.2597 20.3324 18.5118 19.9299 18.9155 19.8372C19.6734 19.6631 20.4413 19.5151 21.2181 19.3942C22.6453 19.172 24.1025 19.0414 25.5834 19.0084V18.75C25.5834 18.3358 25.9192 18 26.3334 18ZM21.3334 23.5431L20.2533 28.3304C20.593 28.4404 20.9558 28.5 21.3334 28.5C21.711 28.5 22.0738 28.4404 22.4135 28.3304L21.3334 23.5431ZM31.3334 23.5431L30.2533 28.3304C30.593 28.4404 30.9558 28.5 31.3334 28.5C31.7111 28.5 32.0738 28.4404 32.4135 28.3304L31.3334 23.5431Z" fill="#5D46EB"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    31 %
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        Estimated waste volume
                                    </span>
                                    <span class="inline-block-span">
                                        missing
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )
            
        with col3:
            st.markdown(
                """
                    <div class="multi-item-callout illustration-container">
                        <div class="item tab-mini-callout">
                            <div class="illustration">
                                <img src="app/static/Illustration-ReducePickups.gif" alt="Go Circular" />
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="text-wrapper">
                                <div class="header">
                                    Bales and presses can optimise pickups and costs
                                </div>
                                <div class="text">
                                    On average compressing waste can reduce waste volume by 4-6 times and
                                    thereby avoid pick-ups and emissions. At a large enough quantity,
                                    compressing your own bales can get you better conditions with your recyclers.
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )

        st.write("")

    with tab4:
        st.markdown(
                """
                    <div class="tab-callout-container">
                        <div class="title">You are collecting 11 materials on average</div>
                        <div class="text sub-header-text">On average Resourcify users have 27 materials. Depending on your available space, there might be room for more granular sorting.</div>
                        <a class="link-btn-primary" href='https://circularity.demo.enterprise.resourcify.de/circular-future' target='_blank'>
                            Order new container
                        </a>
                    </div>
                """,
                unsafe_allow_html=True)
        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:

            st.markdown(
                """
                    <div class="multi-item-callout">
                        <div class="item tab-mini-callout">
                            <div class="icon">
                                <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M31.3622 21.2136C34.2427 22.5007 36.25 25.3908 36.25 28.7497C36.25 33.306 32.5563 36.9997 28 36.9997C23.4437 36.9997 19.75 33.306 19.75 28.7497C19.75 26.5376 20.6206 24.5289 22.0378 23.0475C22.8043 24.1179 23.8205 24.9973 25.0012 25.6006C25.0463 22.825 26.348 20.3548 28.3621 18.7341C29.1255 19.7579 30.1379 20.6182 31.3622 21.2136Z" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M28 34C30.0711 34 31.75 32.3211 31.75 30.25C31.75 28.3467 30.3321 26.7746 28.4949 26.5324C27.4866 27.437 26.7862 28.6779 26.5703 30.0787C25.7877 29.8874 25.0653 29.5425 24.4368 29.0779C24.3156 29.4467 24.25 29.8407 24.25 30.25C24.25 32.3211 25.9289 34 28 34Z" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    34% 
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        of your waste is mixed waste going to
                                    </span>
                                    <span class="inline-block-span">
                                        incineration
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="icon">
                               <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="56" height="56" rx="8" fill="#E9E7D2"/>
                                    <path d="M18.25 31C18.25 33.4853 20.2647 35.5 22.75 35.5H34C36.0711 35.5 37.75 33.8211 37.75 31.75C37.75 30.1479 36.7453 28.7805 35.3316 28.2433C35.4407 27.9324 35.5 27.5981 35.5 27.25C35.5 25.5931 34.1569 24.25 32.5 24.25C32.1767 24.25 31.8654 24.3011 31.5737 24.3957C30.9765 22.1526 28.9312 20.5 26.5 20.5C23.6005 20.5 21.25 22.8505 21.25 25.75C21.25 26.0832 21.281 26.4092 21.3404 26.7252C19.5456 27.3167 18.25 29.0071 18.25 31Z" stroke="#264B4B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                            <div class="text-wrapper">
                                <div class="header">
                                    Up to 456kg of extra CO2
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        emitted for every ton of waste incinerated and
                                    </span>
                                    <span class="inline-block-span">
                                        not recycled
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                    <div class="multi-item-callout illustration-container">
                        <div class="item tab-mini-callout">
                            <div class="illustration">
                                <img src="app/static/Illustration-Sorting.gif" alt="Go Circular" />
                            </div>
                        </div>
                        <div class="item tab-mini-callout">
                            <div class="text-wrapper">
                                <div class="header">
                                    Your employees can help by sorting better
                                </div>
                                <div class="text">
                                    <span class="inline-block-span">
                                        On average there is 27.6% of valuables in residual waste.
                                    </span>
                                    <span class="inline-block-span">
                                        Better sorting can save you costs and emissions by recycling more and incinerating less.
                                    </span>
                                    The majority of our customers run regular waste trainings for their employees and discuss wrongly sorted waste.
                                </div>
                            </div>
                        </div>
                    </div>

                """,
                unsafe_allow_html=True
            )
        st.write("")

page_identify_ways_to_reduce_emissions()

if st.button("Continue", key="next_button", type='primary'):
    st.switch_page("pages/page_3.py")


transparent_footer = """
                    <div class="transparent-footer-spacing"></div>
                """
st.markdown(transparent_footer, unsafe_allow_html=True)
