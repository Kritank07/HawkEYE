import streamlit as st

def header_home():
    logo_path = "https://res.cloudinary.com/hunglbma/image/upload/v1788931463/Gemini_Generated_Image_iux2niiux2niiux2-Photoroom.png"

    st.markdown(f"""

        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 10px;">
            <img src="{logo_path}" alt="Logo" style="height: 100px; margin-top : 0px;" />
            <h1 style = "text-align:center; color:#E0E3FF;">HawkEYE</h1>
        </div>

                """, unsafe_allow_html=True)