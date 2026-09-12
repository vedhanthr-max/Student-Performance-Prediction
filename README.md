# 🎓 Student Performance Prediction using Supervised Machine Learning

A Flask web application that predicts student performance using multiple supervised machine learning algorithms and compares their accuracy to identify the best-performing model.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Project Overview

This project predicts student performance using **7 different supervised machine learning algorithms** and automatically selects the best-performing model. A **Flask web application** provides a simple user interface where users can enter student details and receive instant predictions.

The system classifies students into three categories:
- ❌ **Fail**
- ✅ **Pass**
- 🌟 **Excellent**

---

## 🚀 Features

- ✅ Student Performance Prediction
- ✅ Comparison of 7 Machine Learning Algorithms
- ✅ Automatic Best Model Selection
- ✅ Accuracy Comparison Graph
- ✅ Flask Web Application
- ✅ User-Friendly Interface
- ✅ Model Persistence using Joblib

---

## 🛠 Technologies Used

| Category | Technologies |
|----------|-------------|
| **Language** | Python |
| **Web Framework** | Flask |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Model Saving** | Joblib |

---

## 🤖 Machine Learning Algorithms

The project trains and compares **7 different algorithms**:

1. **Logistic Regression** ← Best performer (100% accuracy)
2. **Decision Tree Classifier**
3. **Random Forest Classifier**
4. **K-Nearest Neighbors (KNN)**
5. **Support Vector Machine (SVM)**
6. **Naive Bayes (Gaussian)**
7. **XGBoost Classifier**

The algorithm with the **highest accuracy** is automatically selected and saved as `model.pkl`.

---

## 📊 Input Parameters

| Parameter | Description | Range |
|-----------|-------------|-------|
| **Study Hours** | Daily study hours | 1 - 10 |
| **Attendance** | Attendance percentage | 50 - 100 |
| **Assignment Marks** | Assignment score | 5 - 25 |
| **Internal Marks** | Internal exam marks | 10 - 50 |

---

## 📈 Output Classes

| Class | Label | Meaning |
|-------|-------|---------|
| 0 | ❌ Fail | Needs significant improvement |
| 1 | ✅ Pass | Meets minimum requirements |
| 2 | 🌟 Excellent | Outstanding performance |

---

## 📂 Project Structure

```
Student-Performance-Prediction/
│
├── app.py                      # Flask web application
├── main.py                     # Model training script
├── generate_dataset.py         # Dataset generator
├── dataset.csv                 # Training dataset (300 records)
├── model.pkl                   # Saved best model
├── requirements.txt            # Dependencies
├── README.md
│
├── static/
│   └── accuracy_graph.png      # Algorithm comparison chart
│
├── templates/
│   ├── index.html              # Input form
│   └── result.html             # Prediction result
│
└── screenshots/
    ├── input_form.png
    ├── result.png
    └── accuracy_graph.png
```

---

## 📸 Screenshots

### 🖥️ Input Form
![Input Form](screenshots/input_form.png)

*User enters Study Hours, Attendance, Assignment Marks, and Internal Marks*

---

### 🎯 Prediction Result
![Prediction Result](screenshots/result.png)

*System displays prediction (Excellent 🌟) along with best algorithm and accuracy*

---

### 📊 Algorithm Accuracy Comparison
![Algorithm Comparison](screenshots/accuracy_graph.png)

*Bar chart comparing accuracy of all 7 machine learning algorithms*

---

## 🚀 How to Run

### 1. Install Libraries

```bash
pip install -r requirements.txt
```

### 2. Generate Dataset (Optional)

```bash
python generate_dataset.py
```

### 3. Train the Model

```bash
python main.py
```

This will:
- Load `dataset.csv`
- Train 7 ML algorithms
- Compare accuracies
- Save the best model as `model.pkl`
- Generate `static/accuracy_graph.png`

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

Enter student details and click **Predict** to see the result.

---

## 🧠 How It Works

### Step 1: Data Generation
`generate_dataset.py` creates 300 synthetic student records with:
- Study Hours (1-10)
- Attendance (50-100)
- Assignment Marks (5-25)
- Internal Marks (10-50)

### Step 2: Model Training
`main.py` trains 7 different ML algorithms and compares their accuracy.

### Step 3: Best Model Selection
The algorithm with the highest accuracy is automatically saved as `model.pkl`.

### Step 4: Prediction
`app.py` loads the saved model and predicts student performance based on user input.

---

## 📊 Accuracy Comparison

The project generates a bar chart comparing all 7 algorithms:

| Algorithm | Accuracy |
|-----------|----------|
| Logistic Regression | 100% ⭐ |
| Random Forest | ~95% |
| Naive Bayes | ~93% |
| XGBoost | ~93% |
| Decision Tree | ~88% |
| SVM | ~86% |
| KNN | ~85% |

**Best Model: Logistic Regression** — automatically saved and used for predictions.

---

## 🔧 Requirements

```
flask
pandas
numpy
matplotlib
scikit-learn
xgboost
joblib
```

Install all at once:

```bash
pip install flask pandas numpy matplotlib scikit-learn xgboost joblib
```

---

## 🔮 Future Enhancements

- [ ] Add more ML algorithms (CatBoost, LightGBM)
- [ ] Deploy on cloud (Render / Railway / Heroku)
- [ ] Add user authentication
- [ ] Store prediction history in database
- [ ] Add data visualization dashboard
- [ ] Support CSV bulk upload for predictions
- [ ] Add model explainability (SHAP/LIME)
- [ ] Improve UI with Bootstrap

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Vedhanth R**

- 🎓 B.E. Computer Science & Engineering
- 🏫 CARE College of Engineering, Tiruchirappalli
- 📧 vedhanth.r65@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/vedhanth-r-226898412)
- 🐙 [GitHub](https://github.com/vedhanthr-max)

---

## 🙏 Acknowledgments

- CARE College of Engineering for academic support
- Scikit-learn & XGBoost documentation
- Flask community

---

## ⭐ Show Your Support

If this project helped you, please give it a **⭐ star** on GitHub!

---

**Made with ❤️ by Vedhanth R**
