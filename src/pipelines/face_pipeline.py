import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() # it will tell how many faces are there in the image
    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location() # to detect the shape of the face
    )
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location() # face recognition model
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1) # 1 beacuse to check image only once

    encodings = []

    for face in faces:
        shape = sp(image_np, face) # to get the landmarks of a particular face from a particular image
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) # generate 128 embeddings

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource # To run the function only once It saves computation and time
def get_trained_model():
    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None
    for student in student_db:
        embedding = student.get("face_embedding")

        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(X) == 0:
        return None

    clf = SVC(kernel="linear", probability = True, class_weight = "balanced") # if one person has 15 images and other has 1 then the 15 images is treated as 1 to maintain a balance and overfit

    try:
        clf.fit(X, y)
    except ValueError:
        pass

    return {"clf" : clf, "X":X, "y":y}

def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendence(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings) # [] => list of student

    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students) >= 2:
            predicted_id = int (clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embedding - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)