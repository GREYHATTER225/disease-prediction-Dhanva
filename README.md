# ⚡🩺 DISEASE PREDICTION & TELEHEALTH PLATFORM

<img align="right" alt="Dhanva GIF" src="templates/dhanva.gif" width="200">

<p align="center">
  <img src="https://img.shields.io/badge/Django-3.0.3-0f0f1a?style=for-the-badge&logo=django&logoColor=00ffea"/>
  <img src="https://img.shields.io/badge/Python-3.7+-0f0f1a?style=for-the-badge&logo=python&logoColor=ff00ff"/>
  <img src="https://img.shields.io/badge/ML-ScikitLearn-0f0f1a?style=for-the-badge&logo=scikit-learn&logoColor=00ffff"/>
  <img src="https://img.shields.io/badge/License-Apache--2.0-0f0f1a?style=for-the-badge&logo=apache&logoColor=ffcc00"/>
</p>

---

> 💊 **AI-Powered Diagnosis meets Real-Time Telehealth**
> ⚡ Built for speed, accessibility, and modern healthcare workflows

---

# 🌌 ░▒▓ OVERVIEW ▓▒░

A **full-stack cyber-ready healthcare platform** that merges:

```
⚡ Machine Learning → Disease Prediction
💬 Real-Time Chat → Doctor Consultation
📅 Smart Scheduling → Appointment Booking
```

🧠 Enter symptoms → Get predictions → Connect with doctors instantly

---

# 🚨 ░▒▓ PROBLEM ▓▒░

```
❌ Limited healthcare access
❌ Expensive consultations  
❌ Long waiting times
❌ Rural accessibility issues
```

---

# ⚡ ░▒▓ SOLUTION ▓▒░

```
✔ Instant ML predictions
✔ Remote doctor access
✔ Real-time chat system
✔ Digital appointment workflow
```

---

# 🧠 ░▒▓ FEATURES ▓▒░

## ⚡ ML ENGINE

* Symptom-based prediction
* Pre-trained scikit-learn model
* Fast inference via joblib

## 👤 AUTH SYSTEM

* Separate login:

  * Patient
  * Doctor
  * Admin

## 🧑‍⚕️ PATIENT MODULE

* Disease prediction
* Appointment booking
* Consultation history
* Profile system

## 🏥 DOCTOR MODULE

* Dashboard
* Patient tracking
* Consultation management

## 💬 CHAT SYSTEM

* Patient ↔ Doctor messaging
* Consultation-based interaction

## 📅 APPOINTMENTS

* Time-slot scheduling
* Doctor mapping

## 🎨 UI SYSTEM

* Bootstrap responsive UI
* Mobile-friendly design

---

# 🧬 ░▒▓ SYSTEM FLOW ▓▒░

```
[ User Symptoms ]
        ↓
[ ML Model ]
        ↓
[ Disease Prediction ]
        ↓
[ Doctor Consultation ]
        ↓
[ Chat + Appointment ]
```

---

# 🧰 ░▒▓ TECH STACK ▓▒░

| Layer       | Tech                  |
| ----------- | --------------------- |
| ⚙ Backend   | Django 3.0.3          |
| 🧠 ML       | scikit-learn          |
| 💾 Storage  | joblib                |
| 🗄 DB       | SQLite                |
| 🎨 Frontend | HTML + Bootstrap + JS |
| 🔐 Auth     | Django Auth           |

---

# 📸 ░▒▓ LIVE DEMO ▓▒░

| Role | Login | Dashboard | Key Features |
|------|-------|-----------|--------------|
| **Patient** | ![Login](screenshots/Patient/patientlogin.png) | ![Dashboard](screenshots/Patient/pacdashbo.png) | ![Signup](screenshots/Patient/patientsignup.png) ![Disease](screenshots/Patient/diagnostics.png) ![Chat](screenshots/Patient/chat.png) ![History](screenshots/Patient/consultationhist.png) |
| **Doctor** | ![Login](screenshots/doctor/doctorlogin.png) | ![Dashboard](screenshots/doctor/docdashbo.png) | ![Signup](screenshots/doctor/doctsignup.png) ![History](screenshots/doctor/consultationhist.png) |
| **Admin** | ![Login](screenshots/admin/adminlogin.png) | ![Dashboard](screenshots/admin/admindashbo.png) | Django Admin |

---

# 📂 ░▒▓ PROJECT STRUCTURE ▓▒░

```
Disease-Prediction/
│
├── manage.py
├── requirements.txt
│
├── disease_prediction/
│   ├── settings.py
│   ├── urls.py
│
├── accounts/     # Authentication
├── main_app/     # Core logic
├── chats/        # Messaging
│
├── templates/    # UI
└── screenshots/  # Demos
```

---

# ⚙️ ░▒▓ INSTALLATION ▓▒░

```bash
git clone <repo>
cd Disease-Prediction

python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

🌐 **http://127.0.0.1:8000/**

---

# 🔑 ░▒▓ LOGIN CREDENTIALS ▓▒░

| Username | Password | Role |
|----------|----------|------|
| `ojas` | `1234` | Patient |
| `ojasdoctor` | `1234` | Doctor |
| `admin` | `1234` | Admin |

---

# 📊 ░▒▓ ML MODEL ▓▒░

* **Input:** Symptoms
* **Output:** Disease prediction
* **Dataset:** Kaggle Disease Prediction

---

# 🌐 ░▒▓ ROUTES ▓▒░

| Endpoint | Description |
|----------|-------------|
| `/` | Homepage |
| `/login/` | Auth |
| `/predict/` | ML |
| `/chat/` | Messaging |

---

# ⚠️ ░▒▓ STATUS ▓▒░

```
✅ ML Prediction
✅ Authentication  
✅ Chat System
🔄 Appointments
🔄 Enhancements
```

---

# 🤝 ░▒▓ CONTRIBUTING ▓▒░

```bash
fork → branch → commit → PR
```

---

# 📜 ░▒▓ LICENSE ▓▒░

**Apache 2.0**

---

# 👨‍💻 ░▒▓ AUTHOR ▓▒░

[Your GitHub]

---
⚡ **Cyberpunk Healthcare** ⚡

# disease-prediction-Dhanva
# disease-prediction-Dhanva
