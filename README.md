# 🎓 Student Performance Prediction & Analytics System

An end-to-end web application that predicts and analyzes student academic performance using Machine Learning and provides actionable insights for students and teachers.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Overview

This project is a **web-based analytics system** designed to help educational institutions track, analyze, and predict student performance. It uses **K-Means Clustering** to group students based on academic patterns and generates **personalized recommendations** for improvement.

The system provides **role-based access** for:
- 👨‍🎓 **Students** — View personal performance and recommendations
- 👩‍🏫 **Teachers** — Manage student data and view class analytics

---

## ✨ Features

### 🎯 Core Features
- ✅ Student data management (CRUD operations)
- ✅ Performance prediction using Machine Learning
- ✅ K-Means clustering for student grouping
- ✅ Automated performance recommendations
- ✅ Interactive analytics dashboard
- ✅ Role-based access (Student / Teacher)

### 📊 Analytics Parameters
- Study hours per day
- Attendance percentage
- Assignment marks
- Internal assessment marks
- Previous academic records

### 📈 Visualizations
- Performance trend charts
- Cluster distribution graphs
- Subject-wise comparison
- Attendance vs. performance correlation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **Database** | SQLite |
| **ML/Analytics** | Scikit-learn, Pandas, NumPy |
| **Visualization** | Matplotlib |
| **Frontend** | HTML, CSS, Bootstrap |
| **Tools** | Git, VS Code, Jupyter |

---

## 🧠 Machine Learning Model

### Algorithm Used: **K-Means Clustering**

**Why K-Means?**
- Groups students with similar performance patterns
- Identifies high, medium, and low performers
- Enables targeted interventions

**Features Used:**
Study Hours

Attendance %

Assignment Marks

Internal Marks

text

**Clusters Formed:**
| Cluster | Description | Action |
|---------|-------------|--------|
| Cluster 0 | High Performers | Advanced materials |
| Cluster 1 | Average Performers | Regular monitoring |
| Cluster 2 | Needs Improvement | Extra support |

---

## 📂 Project Structure
Student-Performance-Prediction/
│
├── app.py # Main Flask application
├── models/
│ ├── ml_model.py # K-Means clustering logic
│ └── predictor.py # Prediction functions
├── database/
│ ├── db.sqlite # SQLite database
│ └── schema.sql # Database schema
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── script.js
│ └── images/
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── student_dashboard.html
│ ├── teacher_dashboard.html
│ └── analytics.html
├── requirements.txt
├── README.md
└── .gitignore

text

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/vedhanthr-max/Student-Performance-Prediction.git
cd Student-Performance-Prediction
2. Create virtual environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies

bash
pip install -r requirements.txt
4. Initialize database

bash
python database/init_db.py
5. Run the application

bash
python app.py
6. Open in browser

text
http://127.0.0.1:5000
📸 Screenshots
Login Page
https://screenshots/login.png

Teacher Dashboard
https://screenshots/teacher_dashboard.png

Student Analytics
https://screenshots/analytics.png

Cluster Visualization
https://screenshots/clusters.png

💡 Add your actual screenshots to a screenshots/ folder in the repo

🔐 Default Credentials (for testing)
Role	Username	Password
Teacher	teacher1	teacher123
Student	student1	student123
⚠️ Change these in production!

📊 API Endpoints
Method	Endpoint	Description
POST	/login	User authentication
GET	/student/dashboard	Student dashboard
GET	/teacher/dashboard	Teacher dashboard
POST	/student/add	Add new student
PUT	/student/update/<id>	Update student data
DELETE	/student/delete/<id>	Delete student
GET	/analytics/clusters	Get cluster data
GET	/analytics/predict/<id>	Predict performance
🧪 Testing
bash
# Run unit tests
python -m pytest tests/

# Run with coverage
pytest --cov=. tests/
🔮 Future Enhancements
□ Add more ML algorithms (Random Forest, XGBoost)
□ Deploy on cloud (Render / Railway / Heroku)
□ Add email notifications for low performers
□ Mobile responsive improvements
□ Export reports to PDF/Excel
□ Real-time chat between teacher and student
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👨‍💻 Author
Vedhanth R

🎓 B.E. Computer Science & Engineering

🏫 CARE College of Engineering, Tiruchirappalli

📧 vedhanth.r65@gmail.com

🔗 LinkedIn

🐙 GitHub

