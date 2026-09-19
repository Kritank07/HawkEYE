import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendence, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student
from PIL import Image
import numpy as np
import time


def student_dashboard():
    st.header("Dashboard Here")


def student_screen():

    style_background_dashboard()
    style_base_layout()

    if 'student_data' in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, gap="xxlarge", vertical_alignment="center")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to Home", type='secondary', key = "loginbackbtn", icon=':material/arrow_back:', icon_position='left'):
            st.session_state["login_type"] = None
            st.rerun()
        
    st.header("Login Using FaceID", text_alignment="center")
    st.space()
    st.space()

    show_registration = False
    photo_source = st.camera_input("Position your face at the center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("AI is Scanning.."):
            detected, all_ids, num_faces = predict_attendence(img)

            if num_faces == 0:
                st.warning("Face Not found")

            elif num_faces > 1:
                st.warning("Multiple Faces Found")

            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face not Recognized! You might be a new Student!")
                    show_registration = True


    if show_registration :
        with st.container(border = True):
            st.header("Register New Profile")
            new_name = st.text_input("Enter Your name", placeholder="Enter your name")

            st.subheader("Optional : Voice Enrollment")
            st.info("Enroll Your Voice for Voice Only Attendence")

            audio_data = None

            try:
                audio_data = st.audio_input("Record a short phrase like 'Hi, my name is Akash and I am present in today's class'")
            except Exception as e:
                st.error("Audio data Failed!")

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating Profile...'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)

                        if encodings:
                            face_emb= encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())
                            response_data = create_student(new_name, face_embedding = face_emb, voice_embedding = voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile Created! Hi {new_name}!")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldn't capture your facial features for registration")
                else:
                    st.warning("Please enter your name!")




    footer_dashboard()