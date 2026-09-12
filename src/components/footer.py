import streamlit as st

def footer_home():
    st.markdown(f"""

        <div style="margin-top: 20px; display: flex; justify-content: center; gap : 6px; item-align:center;">
            <p style = "font-weight: bold; color : white;">Created with ❤️ by the Kritank</p>
        </div>

                """, unsafe_allow_html=True)