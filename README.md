# HawkEYE 🦅 | AI-Powered Attendance System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Flask](https://img.shields.io/badge/Flask-Backend-000000)
![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E)
![License](https://img.shields.io/badge/License-MIT-green)

HawkEYE is a next-generation AI attendance system that replaces manual roll calls with high-speed facial analysis and sequential voice biometrics. It transforms how educators track student presence by eliminating manual data entry and reclaiming valuable teaching time.

🌐 **[Try the Live Application](https://hawkeyelandingpage.vercel.app/)**

---

## 🚀 Key Features

*   **📸 AI Face Analysis:** Scans the room and identifies every student from a single class photo in milliseconds using advanced neural networks.
*   **🎙️ Sequential Voice ID:** A futuristic roll-call where students simply say "Present." The audio-AI matches their unique voice signatures against stored embeddings in real-time.
*   **📱 QR-Driven Rosters:** Course codes generate unique QR codes for instant student enrollment. No more manual entry or data management headaches.
*   **📊 Actionable Dashboard:** Review and manage historical logs, view confidence scores, download CSV reports, and track long-term attendance trends.

## 🛠️ Technology Stack

**Frontend & App Layer:**
*   [Streamlit](https://streamlit.io/) - Reactive frontend architecture for the main application.
*   [Flask](https://flask.palletsprojects.com/) - Robust routing and landing page layer.

**AI & Biometrics:**
*   **Vision:** `FaceRecognition`, `dlib`, and OpenCV for high-fidelity facial biometrics.
*   **Audio:** `Resemblyzer` and `librosa` for extracting and matching unique student voice signatures.

**Backend & Storage:**
*   [Supabase](https://supabase.com/) - Real-time PostgreSQL infrastructure handling secure authentication and unified data sync.
