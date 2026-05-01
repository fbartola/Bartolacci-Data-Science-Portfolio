import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris, load_wine

st.set_page_config(page_title="Unsupervised ML Explorer", layout="wide")

st.title("Unsupervised Machine Learning Explorer")
st.write("Upload a tabular dataset or choose a sample dataset to explore unsupervised machine learning techniques like K-Means Clustering and Principal Component Analysis (PCA).")

# Sidebar for data selection
st.sidebar.header("1. Data Selection")
data_source = st.sidebar.radio("Choose Data Source:", ("Sample Dataset", "Upload CSV"))

df = None
if data_source == "Sample Dataset":
    dataset_name = st.sidebar.selectbox("Select Dataset:", ("Iris", "Wine"))
    if dataset_name == "Iris":
        data = load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
    else:
        data = load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
else:
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")

if df is not None:
    st.header("Dataset Overview")
    st.write(df.head())
    
    # Preprocessing
    st.sidebar.header("2. Preprocessing")
    
    # Only select numeric columns for these models by default
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_columns:
        st.error("The dataset does not contain any numeric columns, which are required for these models.")
    else:
        features = st.sidebar.multiselect("Select Features for Modeling", df.columns.tolist(), default=numeric_columns)
        
        if len(features) < 2:
            st.warning("Please select at least 2 features for modeling and visualization.")
        else:
            X = df[features]
            
            # Handle missing values by simple imputation (mean)
            if X.isnull().sum().sum() > 0:
                st.info("Missing values detected. Imputing with mean values.")
                X = X.fillna(X.mean())

            # Scaling
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            st.sidebar.header("3. Model Selection")
            model_type = st.sidebar.selectbox("Select Model:", ("K-Means Clustering", "Principal Component Analysis (PCA)"))

            if model_type == "K-Means Clustering":
                st.subheader("K-Means Clustering")
                st.write("K-Means groups data into $k$ distinct clusters based on feature similarity.")
                
                k = st.sidebar.slider("Number of Clusters (k)", min_value=2, max_value=10, value=3)
                
                # Elbow Method
                st.markdown("### Finding Optimal k (Elbow Method)")
                st.write("The elbow method helps to determine the optimal number of clusters by fitting the model with a range of values for k and plotting the inertia (sum of squared distances of samples to their closest cluster center).")
                if st.button("Generate Elbow Plot"):
                    inertias = []
                    k_range = range(1, 11)
                    for i in k_range:
                        kmeans_temp = KMeans(n_clusters=i, random_state=42, n_init=10)
                        kmeans_temp.fit(X_scaled)
                        inertias.append(kmeans_temp.inertia_)
                    
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.plot(k_range, inertias, marker='o', linestyle='--')
                    ax.set_title("Elbow Method for Optimal k")
                    ax.set_xlabel("Number of Clusters (k)")
                    ax.set_ylabel("Inertia")
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                
                # Train model
                kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
                clusters = kmeans.fit_predict(X_scaled)
                df_with_clusters = df.copy()
                df_with_clusters['Cluster'] = clusters
                
                # Performance Metric
                silhouette_avg = silhouette_score(X_scaled, clusters)
                
                st.markdown("### Model Performance")
                col1, col2 = st.columns(2)
                col1.metric("Silhouette Score", f"{silhouette_avg:.4f}")
                col2.markdown("*A higher silhouette score indicates better defined clusters (range: -1 to 1).*")
                
                # Visualization
                st.markdown("### Cluster Visualization")
                st.write("Visualizing clusters in 2D space. If there are >2 features, PCA is used to project them into 2 dimensions.")
                
                if len(features) > 2:
                    pca_2d = PCA(n_components=2)
                    X_2d = pca_2d.fit_transform(X_scaled)
                    plot_df = pd.DataFrame(X_2d, columns=['PC1', 'PC2'])
                else:
                    plot_df = X.copy()
                    plot_df.columns = ['PC1', 'PC2']
                
                plot_df['Cluster'] = clusters.astype(str)
                
                fig2, ax2 = plt.subplots(figsize=(8, 6))
                sns.scatterplot(data=plot_df, x='PC1', y='PC2', hue='Cluster', palette='viridis', ax=ax2, s=100, alpha=0.8)
                ax2.set_title(f"Clusters Visualization (k={k})")
                ax2.grid(True, alpha=0.3)
                st.pyplot(fig2)
                
                st.markdown("### Data with Cluster Labels")
                st.dataframe(df_with_clusters)

            elif model_type == "Principal Component Analysis (PCA)":
                st.subheader("Principal Component Analysis (PCA)")
                st.write("PCA reduces the dimensionality of the dataset while preserving as much variance as possible.")
                
                max_components = min(len(features), 10)
                n_components = st.sidebar.slider("Number of Components", min_value=1, max_value=max_components, value=min(2, max_components))
                
                pca = PCA(n_components=n_components)
                X_pca = pca.fit_transform(X_scaled)
                
                # Explained Variance
                st.markdown("### Explained Variance")
                fig3, ax3 = plt.subplots(figsize=(8, 4))
                ax3.bar(range(1, n_components + 1), pca.explained_variance_ratio_, alpha=0.7, label='Individual')
                ax3.plot(range(1, n_components + 1), np.cumsum(pca.explained_variance_ratio_), marker='o', color='red', label='Cumulative')
                ax3.set_title("Explained Variance Ratio per Principal Component")
                ax3.set_xlabel("Principal Component")
                ax3.set_ylabel("Explained Variance Ratio")
                ax3.set_xticks(range(1, n_components + 1))
                ax3.legend()
                ax3.grid(True, alpha=0.3)
                st.pyplot(fig3)
                
                total_var = np.sum(pca.explained_variance_ratio_) * 100
                st.write(f"**Total variance explained by {n_components} components:** {total_var:.2f}%")
                
                # 2D PCA Plot
                if n_components >= 2:
                    st.markdown("### 2D PCA Scatter Plot")
                    pca_df = pd.DataFrame(X_pca[:, :2], columns=['PC1', 'PC2'])
                    fig4, ax4 = plt.subplots(figsize=(8, 6))
                    sns.scatterplot(data=pca_df, x='PC1', y='PC2', ax=ax4, s=100, alpha=0.8)
                    ax4.set_title("Data Projected onto First Two Principal Components")
                    ax4.grid(True, alpha=0.3)
                    st.pyplot(fig4)
                else:
                    st.info("Select at least 2 components to view the 2D scatter plot.")
                    
                st.markdown("### Transformed Data (PCA Components)")
                pca_df_all = pd.DataFrame(X_pca, columns=[f'PC{i+1}' for i in range(n_components)])
                st.dataframe(pca_df_all)
else:
    st.info("Please select a data source from the sidebar to begin.")
