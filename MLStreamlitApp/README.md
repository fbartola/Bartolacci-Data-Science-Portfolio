<div align="center">

# 🧠 Supervised ML Playground

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)]()

> *An interactive web application built with Streamlit to visually explore and intuition-build around supervised machine learning models.*

**[🚀 Play with the Live App Here!](https://bartolacci-data-science-portfolio-lkmfmnwxdcsj3y5odkaqqz.streamlit.app/)**

---

</div>

## ✨ Project Overview

The **Supervised ML Playground** allows you to see how machine learning works under the hood. Upload your data, tweak model settings (hyperparameters), and instantly visualize how those choices impact model accuracy, precision, and error rates.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed. You'll need the following core libraries:
`streamlit`, `pandas`, `numpy`, `scikit-learn`, `matplotlib`, and `seaborn`.

### Run Locally

1️⃣ **Clone the repository**
```bash
git clone https://github.com/francescabartolacci/Bartolacci-Data-Science-Portfolio.git
cd Bartolacci-Data-Science-Portfolio
```

2️⃣ **Install dependencies**
```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

3️⃣ **Launch the app**
```bash
streamlit run MLApp.py
```

---

## 🛠️ App Features

### 📊 Data Selection
- **Built-in Datasets:** Instantly load standard datasets like *Breast Cancer*, *Iris*, and *Diabetes*.
- **Custom Uploads:** Upload your own `.csv` file and manually map the target variable.

### 🤖 Models & Hyperparameters
Easily adjust settings via sidebar sliders to see real-time updates:

🟣 **Classification**
- **Logistic Regression:**
  - *Tunable:* Regularization (`C`), Test Split Size
  - *Hyperparameter Details:* The **C (Regularization Inverse)** parameter controls how much the model is penalized for having large weights. A smaller `C` increases regularization, helping to prevent overfitting by making the model simpler.

- **Random Forest Classifier:**
  - *Tunable:* Number of Trees, Max Depth, Test Split Size
  - *Hyperparameter Details:* **Number of Trees** determines how many decision trees are built; more trees typically increase accuracy and stability but take longer to train. **Max Depth** controls how deep each tree can grow; limiting depth helps prevent the model from memorizing the training data (overfitting).

🟢 **Regression**
- **Linear Regression:**
  - *Tunable:* Test Split Size
  - *Hyperparameter Details:* Linear Regression is a straightforward model with no core hyperparameters to tune besides how much data is held out for the test set.

- **Random Forest Regressor:**
  - *Tunable:* Number of Trees, Max Depth, Test Split Size
  - *Hyperparameter Details:* Similar to classification, tuning **Number of Trees** and **Max Depth** allows you to balance between a model that captures complex non-linear trends and one that generalizes well to unseen data.


---

## 📚 References
This project was built with the help of these incredible resources:
- 📖 [Streamlit Documentation](https://docs.streamlit.io/)
- ⚙️ [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
- 🎨 [Seaborn Customization Guide](https://seaborn.pydata.org/tutorial/customization.html)
