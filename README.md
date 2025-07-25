
# 🎓 Student Performance Prediction Pipeline

A machine learning project designed to predict student academic performance based on various demographic and academic factors. This project involves data preprocessing, feature engineering, model training, evaluation, and Docker-based deployment.

---

## 🚀 Features

- 🧪 Exploratory Data Analysis (EDA) on student performance dataset
- 🛠️ Feature engineering and preprocessing pipeline
- 🧠 Trained multiple ML models for classification
- ✅ Model evaluation using accuracy, confusion matrix, and cross-validation
- 🐳 Dockerized application for scalable deployment

---

## 🧠 Tech Stack

| Component     | Tech Used             |
|---------------|------------------------|
| Language      | Python                 |
| ML Libraries  | Scikit-learn, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn    |
| Deployment    | Docker                 |
| Version Ctrl  | Git, GitHub            |

---

## 📊 Dataset

- Source: [UCI / Kaggle Student Performance Dataset]
- Features include: study time, failures, absences, family background, and academic grades
- Target: Final grade classification (Pass/Fail or categorical scores)

---

## ⚙️ How to Run

```bash
git clone https://github.com/yourusername/student-performance-prediction.git
cd student-performance-prediction
pip install -r requirements.txt
python app.py
```

For Docker deployment:

```bash
docker build -t student-performance-app .
docker run -p 8501:8501 student-performance-app
```

---

## 📁 Project Structure

```
student-performance-prediction/
├── data/
├── models/
├── app.py
├── pipeline.py
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## 📊 Model Evaluation

- Models Used: Logistic Regression, Random Forest, Decision Tree
- Best accuracy achieved: **89%**
- Used stratified split and K-fold validation

---

## 📸 Screenshots

*(Add graphs showing feature importance, confusion matrix, and UI if applicable)*

---

## 📬 Contact

**Manish Thakur**  
[LinkedIn](https://www.linkedin.com/in/manish-thakur-2b3176236) | [GitHub](https://github.com/mrx000777)

---

## 🏷️ Tags

`Student ML` `Education Analytics` `Classification Model` `Data Science` `Docker`
