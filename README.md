# 🎓 Student Performance Prediction Using Multiple Linear Regression

## 📖 Overview

This project is a Machine Learning application that predicts a student's performance based on various academic and lifestyle factors. The model is built using **Multiple Linear Regression (MLR)** and deployed using **Flask** to provide real-time predictions through a simple web interface.

The application helps analyze how factors such as study hours, previous scores, extracurricular activities, sleep hours, and practice questions influence a student's academic performance.

---

## 🚀 Features

✅ Data Preprocessing and Feature Engineering

✅ Multiple Linear Regression Model

✅ Object-Oriented Programming (OOP) Implementation

✅ Model Evaluation using R² Score, MSE, and RMSE

✅ Model Saving and Loading using Pickle

✅ Flask-Based Web Application

✅ Real-Time Performance Prediction

---

## 📊 Dataset Information

The model uses the following features:

| Feature | Description |
|----------|-------------|
| Hours Studied | Number of hours studied per day |
| Previous Scores | Previous examination scores |
| Extracurricular Activities | Participation in extracurricular activities |
| Sleep Hours | Average daily sleep hours |
| Sample Question Papers Practiced | Number of practice questions solved |

### 🎯 Target Variable

**Performance Index** – Predicted Student Performance Score

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Flask
- Pickle
- HTML
- CSS

---

## 📂 Project Structure

```bash
Student-Performance-Prediction/
│
├── app.py
├── oops.py
├── Model_pkl.pkl
├── templates/
│   └── index.html
│
├── Student_Performance.csv
│
└── README.md
```

---

## ⚙️ Workflow

### 1. Data Preprocessing

- Load dataset
- Handle categorical data using One-Hot Encoding
- Feature selection
- Train-Test split

### 2. Model Training

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

### 3. Model Evaluation

The model is evaluated using:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### 4. Model Saving

```python
with open("Model_pkl.pkl", "wb") as f:
    pickle.dump(model, f)
```

### 5. Deployment

The trained model is deployed using Flask for real-time predictions.

---

## 📈 Performance Metrics

### R² Score

Measures how well the model explains the variance in the target variable.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

### Root Mean Squared Error (RMSE)

Measures prediction error in the original scale of the target variable.

---

## 🎯 Sample Prediction

### Input

```text
Hours Studied = 5
Previous Score = 70
Extracurricular Activities = Yes
Sleep Hours = 7
Practice Questions = 5
```

### Output

```text
Predicted Performance Index = XX.XX
```

---

## 🌐 Running the Application

### Clone the Repository

```bash
git clone https://github.com/your-username/Student-Performance-Prediction.git
```

### Navigate to the Project Directory

```bash
cd Student-Performance-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```




## 🎓 Key Learnings

Through this project, I gained hands-on experience in:

- Multiple Linear Regression
- Machine Learning Workflow
- Data Preprocessing
- Model Evaluation Techniques
- Object-Oriented Programming
- Flask Web Development
- Model Deployment

---

## 👨‍💻 Author

**Manoj Kumar**

Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer

### Connect With Me

- GitHub: https://github.com/Larson-8
- LinkedIn: https://www.linkedin.com/in/manoj-kumar-balisetty-53794b256/

---
