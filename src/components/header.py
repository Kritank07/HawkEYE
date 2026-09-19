import streamlit as st

def header_home():
    logo_path = "https://res.cloudinary.com/hunglbma/image/upload/v1789211173/copy_of_gemini_generated_image_x23tctx23tctx23t.png"

    st.markdown(f"""

        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 10px;">
            <img src="{logo_path}" alt="Logo" style="height: 100px; margin-top : 0px;" />
            <h1 style = "text-align:center; color:#102A43;">HawkEYE</h1>
        </div>

                """, unsafe_allow_html=True)


def header_dashboard():
    logo_path = "https://res.cloudinary.com/hunglbma/image/upload/v1789211173/copy_of_gemini_generated_image_x23tctx23tctx23t.png"

    st.markdown(f"""

        <div style="display: flex; align-items: center; justify-content: center; gap:10px;">
            <img src="{logo_path}" alt="Logo" style="height: 85px;"/>
            <h2 style = "text-align:left; color:#102A43;">Hawk<br/>EYE</h2>
        </div>

                """, unsafe_allow_html=True)
