import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    /* Warm ivory makes the landing page distinct and suits the logo's gold accents. */
                    background: #FFF7E8 !important;
                    color: #102A43 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#FFFFFF !important;
                    padding:2rem !important;
                    border-radius: 5rem !important;
                    box-shadow: 0 12px 30px rgba(30, 64, 110, 0.12) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    /* Keep dashboard screens visually consistent with the home page. */
                    background: #EAF2FF !important;
                    color: #102A43 !important;
                }

                .stApp label p {
                    color: #102A43 !important;
                    font-weight: 600 !important;
                }

                /* Streamlit text inputs use BaseWeb wrappers as well as input tags. */
                /* The visible outline is applied to Streamlit's outer BaseWeb input. */
                .stApp [data-testid="stTextInput"] div[data-baseweb="input"],
                .stApp [data-testid="stTextInput"] div[data-baseweb="base-input"] {
                    background-color: #FFFFFF !important;
                    border: none !important;
                    box-shadow: none !important;
                    outline: none !important;
                }

                .stApp [data-testid="stTextInput"] div[data-baseweb="input"] > div,
                .stApp [data-testid="stTextInput"] div[data-baseweb="base-input"] > div {
                    background-color: #FFFFFF !important;
                    border: none !important;
                    box-shadow: none !important;
                }

                .stApp input,
                .stApp textarea {
                    background-color: #FFFFFF !important;
                    color: #102A43 !important;
                    caret-color: #102A43 !important;
                    border: none !important;
                    border-radius: 0.75rem !important;
                    box-shadow: none !important;
                }

                .stApp input::placeholder,
                .stApp textarea::placeholder {
                    color: #66788A !important;
                    opacity: 1 !important;
                }

                /* A quiet separator between form inputs and their actions. */
                .stApp hr {
                    border-color: #C7D8EC !important;
                    margin: 1.75rem 0 !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #102A43 !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 1.85rem !important;
                font-weight: 400 !important;
                line-height:1.08 !important;
                letter-spacing: 0.015em !important;
                margin-bottom:0rem !important;
                color : #102A43 !important;
            }
                
            h3, h4, p, .stMarkdown, .stText {
                font-family: 'Outfit', sans-serif;    
                color: #102A43 !important;
            }

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            /* Keep button labels readable even though general body text is navy. */
            button, button * {
                color: #FFFFFF !important;
            }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)
