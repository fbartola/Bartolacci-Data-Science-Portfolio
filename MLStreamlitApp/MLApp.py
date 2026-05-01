import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, 
                             roc_curve, auc, confusion_matrix, 
                             mean_squared_error, mean_absolute_error, r2_score)
from sklearn.datasets import load_iris, load_diabetes, load_breast_cancer

st.set_page_config(page_title="Supervised ML Playground", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    .stApp {
        background-color: #f7f9fc;
        color: #1a1a2e;
    }
    h1, h2, h3 {
        color: #0f4c75;
        font-family: 'Inter', sans-serif;
    }
    .stButton>button {
        background-color: #3282b8;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0f4c75;
        transform: scale(1.02);
    }
    .metric-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-bottom: 20px;
        border-top: 4px solid #3282b8;
    }
    .metric-title {
        font-size: 1.1rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1a1a2e;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Supervised Machine Learning Playground")
st.markdown("""
Welcome to the interactive Machine Learning playground! Select a dataset, configure hyperparameters, 
and observe how your choices affect the model's performance. Perfect for intuition building and exploration.
""")

with st.sidebar:
    st.header("⚙️ Configuration")
    
    st.subheader("1. Data Selection")
    data_source = st.radio("Choose Data Source", ("Sample Dataset", "Upload CSV"))
    
    df = None
    target_col = None
    problem_type = None
    if data_source == "Sample Dataset":
        sample_dataset = st.selectbox("Select Dataset", ("Breast Cancer (Classification)", "Iris (Classification)", "Diabetes (Regression)"))
        if sample_dataset == "Iris (Classification)":
            data = load_iris()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['target'] = data.target
            # Name target properly for Iris
            df['target'] = df['target'].map(dict(enumerate(data.target_names)))
            target_col = 'target'
            problem_type = "Classification"
        elif sample_dataset == "Breast Cancer (Classification)":
            data = load_breast_cancer()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['target'] = data.target
            target_col = 'target'
            problem_type = "Classification"
        else:
            data = load_diabetes()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df['target'] = data.target
            target_col = 'target'
            problem_type = "Regression"
    else:
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            target_col = st.selectbox("Select Target Variable", df.columns)
            problem_type = st.radio("Select Problem Type", ("Classification", "Regression"))
            
    if df is not None:
        st.subheader("2. Model Selection")
        if problem_type == "Classification":
            model_algo = st.selectbox("Select Algorithm", ("Logistic Regression", "Random Forest Classifier"))
            if model_algo == "Logistic Regression":
                st.info("💡 **Logistic Regression** is a linear model used for binary or multi-class classification. It estimates probabilities using a logistic function. Great for linearly separable data.")
            else:
                st.info("💡 **Random Forest** is an ensemble method that builds multiple decision trees and merges them together for a more accurate and stable prediction. It handles non-linear relationships well.")
        else:
            model_algo = st.selectbox("Select Algorithm", ("Linear Regression", "Random Forest Regressor"))
            if model_algo == "Linear Regression":
                st.info("💡 **Linear Regression** is a simple model that assumes a linear relationship between the input features and the target continuous variable.")
            else:
                st.info("💡 **Random Forest Regressor** uses an ensemble of decision trees to predict continuous values, capturing complex non-linear relationships without assuming linearity.")
            
        st.subheader("3. Hyperparameters")
        test_size = st.slider("Test Set Size (%)", 10, 50, 20, 5) / 100.0
        
    
        hyperparameters = {}
        if model_algo == "Logistic Regression":
            st.markdown("**Hyperparameter Tuning:**")
            C_val = st.slider("Regularization Inverse (C)", 0.01, 10.0, 1.0, 0.01, help="Smaller values specify stronger regularization, preventing overfitting by penalizing large coefficients. Play with this to see how it affects accuracy on the test set!")
            max_iter = st.number_input("Max Iterations", 100, 1000, 200, 50, help="Maximum number of iterations taken for the solvers to converge. If the model fails to converge, try increasing this.")
            hyperparameters = {'C': C_val, 'max_iter': max_iter}
        elif model_algo == "Random Forest Classifier" or model_algo == "Random Forest Regressor":
            st.markdown("**Hyperparameter Tuning:**")
            n_estimators = st.slider("Number of Trees", 10, 500, 100, 10, help="The number of trees in the forest. More trees usually improve performance and stabilize predictions, but slow down training.")
            max_depth = st.slider("Max Depth", 1, 50, 10, 1, help="The maximum depth of the tree. Decreasing this limits the complexity of the model to prevent overfitting, while increasing it allows the model to learn more complex patterns.")
            hyperparameters = {'n_estimators': n_estimators, 'max_depth': max_depth}
        
        run_btn = st.button("🚀 Train Model")

if df is not None:
    st.header("📊 Dataset Overview")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(df.head(10), use_container_width=True)
    with col2:
        st.write(f"**Shape:** {df.shape[0]} rows, {df.shape[1]} columns")
        st.write(f"**Target Variable:** `{target_col}`")
        if st.checkbox("Show Summary Statistics"):
            st.write(df.describe())
            
    if target_col is not None and ('run_btn' in locals() and run_btn):
        st.markdown("---")
        st.header("⚙️ Model Training & Evaluation")
        
        # Prepare Data
        # Drop missing values for simplicity
        df_clean = df.dropna()
        X = df_clean.drop(columns=[target_col])
        y = df_clean[target_col]
        
        # Handle categorical features dynamically
        X = pd.get_dummies(X, drop_first=True)
            
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        
        # Scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Model Training 
        training_successful = False
        with st.spinner("Training model..."):
            try:
                if model_algo == "Logistic Regression":
                    model = LogisticRegression(C=hyperparameters['C'], max_iter=hyperparameters['max_iter'], random_state=42)
                elif model_algo == "Random Forest Classifier":
                    model = RandomForestClassifier(n_estimators=hyperparameters['n_estimators'], max_depth=hyperparameters['max_depth'], random_state=42)
                elif model_algo == "Linear Regression":
                    model = LinearRegression()
                elif model_algo == "Random Forest Regressor":
                    model = RandomForestRegressor(n_estimators=hyperparameters['n_estimators'], max_depth=hyperparameters['max_depth'], random_state=42)
                    
                model.fit(X_train_scaled, y_train)
                y_pred = model.predict(X_test_scaled)
                
                st.toast("Model Trained Successfully!", icon='🎉')
                training_successful = True
                
            except ValueError as e:
                st.error("🚨 There was an issue training the model!")
                st.warning(f"**Error Details:** {e}")
                st.info("💡 **Tip:** This usually happens if you've selected **Classification** for a target column that contains continuous, numerical data. Try switching the Problem Type to **Regression** in the sidebar!")
                
        if training_successful:
            # Display Metrics
            st.subheader("Performance Metrics")
            
            if problem_type == "Classification":
                acc = accuracy_score(y_test, y_pred)
                prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
                rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
                f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
                
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                def metric_box(col, title, value):
                    col.markdown(f'<div class="metric-container"><div class="metric-title">{title}</div><div class="metric-value">{value:.4f}</div></div>', unsafe_allow_html=True)
                metric_box(m_col1, "Accuracy", acc)
                metric_box(m_col2, "Precision", prec)
                metric_box(m_col3, "Recall", rec)
                metric_box(m_col4, "F1-Score", f1)
                
                st.subheader("Visualizations")
                v_col1, v_col2 = st.columns(2)
                
                with v_col1:
                    st.write("**Confusion Matrix**")
                    cm = confusion_matrix(y_test, y_pred)
                    fig_cm, ax_cm = plt.subplots(figsize=(5,4))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax_cm)
                    ax_cm.set_xlabel('Predicted')
                    ax_cm.set_ylabel('Actual')
                    st.pyplot(fig_cm)
                    
                with v_col2:
                    # ROC Curve if binary classification
                    if len(np.unique(y)) == 2 and hasattr(model, "predict_proba"):
                        st.write("**ROC Curve**")
                        # Assuming positive label is the second class from unique sorting
                        pos_label = np.unique(y)[1] 
                        y_test_binary = (y_test == pos_label).astype(int)
                        # For getting positive class probabilities if it's binary
                        if hasattr(model, "classes_"):
                            pos_class_index = np.where(model.classes_ == pos_label)[0][0]
                            y_prob = model.predict_proba(X_test_scaled)[:, pos_class_index]
                        else:
                            y_prob = model.predict_proba(X_test_scaled)[:, 1]
                            
                        fpr, tpr, thresholds = roc_curve(y_test_binary, y_prob)
                        roc_auc = auc(fpr, tpr)
                        
                        fig_roc, ax_roc = plt.subplots(figsize=(5,4))
                        ax_roc.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC AUC = {roc_auc:.2f}')
                        ax_roc.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
                        ax_roc.set_xlim([0.0, 1.0])
                        ax_roc.set_ylim([0.0, 1.05])
                        ax_roc.set_xlabel('False Positive Rate')
                        ax_roc.set_ylabel('True Positive Rate')
                        ax_roc.legend(loc="lower right")
                        st.pyplot(fig_roc)
                    else:
                        st.info("ROC Curve is only plotted for binary classification with probability estimates.")
                        
                st.markdown("---")
                st.markdown("#### 📖 How to Interpret These Metrics")
                st.markdown("""
                - **Accuracy**: The overall percentage of correct predictions. (Formula: Correct / Total)
                - **Precision**: Out of all the positive predictions made, how many were actually correct? *Helps understand false positives.*
                - **Recall**: Out of all actual positive cases, how many did we correctly identify? *Helps understand false negatives.*
                - **F1-Score**: A balanced metric combining both precision and recall. Useful when classes are imbalanced.
                - **Confusion Matrix**: Shows exactly where the model is confusing classes (e.g., predicting Class 1 when it's actually Class 0).
                - **ROC Curve & AUC**: Visualizes the trade-off between the True Positive Rate and False Positive Rate. An Area Under the Curve (AUC) closer to 1.0 indicates an excellent model, while 0.5 is a random guess.
                """)
            else: # Regression
                mse = mean_squared_error(y_test, y_pred)
                mae = mean_absolute_error(y_test, y_pred)
                rmse = np.sqrt(mse)
                r2 = r2_score(y_test, y_pred)
                
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                def metric_box(col, title, value):
                    col.markdown(f'<div class="metric-container"><div class="metric-title">{title}</div><div class="metric-value">{value:.4f}</div></div>', unsafe_allow_html=True)
                metric_box(m_col1, "MSE", mse)
                metric_box(m_col2, "RMSE", rmse)
                metric_box(m_col3, "MAE", mae)
                metric_box(m_col4, "R² Score", r2)
                
                st.subheader("Visualizations")
                st.write("**Actual vs Predicted**")
                fig_reg, ax_reg = plt.subplots(figsize=(8,5))
                ax_reg.scatter(y_test, y_pred, alpha=0.6, color='#3282b8')
                # Draw y=x line properly
                min_val = min(y_test.min(), y_pred.min())
                max_val = max(y_test.max(), y_pred.max())
                ax_reg.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2)
                ax_reg.set_xlabel('Actual Values')
                ax_reg.set_ylabel('Predicted Values')
                st.pyplot(fig_reg)

                st.markdown("---")
                st.markdown("#### 📖 How to Interpret These Metrics")
                st.markdown("""
                - **MSE (Mean Squared Error)**: The average of the squared differences between predicted and actual values. It heavily penalizes larger errors.
                - **RMSE (Root Mean Squared Error)**: The square root of MSE. This brings the error back to the original units of the target variable, making it easier to understand.
                - **MAE (Mean Absolute Error)**: The average absolute difference between predicted and actual values. It is less sensitive to extreme outliers than RMSE.
                - **R² Score**: Represents the proportion of variance in the dependent variable that is predictable from the independent variables. **1.0 is a perfect prediction**, while 0.0 means the model is no better than simply predicting the mean every time.
                - **Actual vs Predicted Plot**: If the model is perfect, all blue dots will fall exactly on the red dashed diagonal line (where Actual = Predicted). Deviations from the line show prediction errors.
                """)
