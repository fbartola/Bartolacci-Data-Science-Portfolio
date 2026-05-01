# Unsupervised Machine Learning Explorer

## Project Overview
The Unsupervised Machine Learning Explorer is an interactive Streamlit application designed to help users experiment with and understand unsupervised machine learning techniques. The goal of this project is to provide a seamless, intuitive interface where users can upload their own tabular data (or select from sample datasets) and immediately see the effects of different models and hyperparameters on their data. 

Through this app, users can visually explore how data points are grouped and how high-dimensional data can be reduced for visualization without writing a single line of code.

## App Features
The application currently supports two primary unsupervised learning models:

1. **K-Means Clustering**
   - **How it works:** K-Means groups data into $k$ distinct clusters based on feature similarity and distance to cluster centroids.
   - **Hyperparameter Tuning:** Users can interactively adjust the number of clusters ($k$) using a slider.
   - **Evaluation & Feedback:** The app generates an **Elbow Plot** (Inertia vs. k) to help users visually determine the optimal number of clusters. It also calculates the **Silhouette Score** to measure how well-defined the clusters are, and visualizes the clustered data in a 2D scatter plot.

2. **Principal Component Analysis (PCA)**
   - **How it works:** PCA is a dimensionality reduction technique that transforms high-dimensional data into fewer dimensions while preserving as much variance (information) as possible.
   - **Hyperparameter Tuning:** Users can use a slider to select the number of principal components they wish to reduce their data to.
   - **Evaluation & Feedback:** The app provides a bar chart of the **Explained Variance Ratio** to show how much information is retained by each principal component, along with a 2D projection scatter plot of the transformed data.

## Instructions

### Running Locally
To run this application on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd MLUnsupervisedApp
   ```

2. **Install the required libraries:**
   It is recommended to use a virtual environment. Install the dependencies using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
   The app will automatically open in your default web browser at `http://localhost:8501`.

### Necessary Libraries and Versions
- `streamlit` (>= 1.32.0)
- `pandas` (>= 1.3.0)
- `numpy` (>= 1.20.0)
- `matplotlib` (>= 3.4.0)
- `seaborn` (>= 0.11.0)
- `scikit-learn` (>= 1.0.0)

### Deployed Version
You can access the live, deployed version of this app on the Streamlit Community Cloud here:
**[Link to Deployed Streamlit App]** *(Replace this with your actual deployed URL)*

## Visual Examples

*(Tip: Once you run your app, take a few screenshots of the visualizations and add them here!)*

- **Elbow Plot for K-Means:**
  ![Elbow Plot Placeholder](https://via.placeholder.com/600x300.png?text=Add+Elbow+Plot+Screenshot+Here)
- **PCA Explained Variance:**
  ![PCA Plot Placeholder](https://via.placeholder.com/600x300.png?text=Add+PCA+Variance+Screenshot+Here)

## References
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-Learn K-Means Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Scikit-Learn PCA Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [Understanding the Silhouette Score](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
