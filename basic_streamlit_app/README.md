# Basic Streamlit App – Penguin Data Filtering

This project is a basic Streamlit app created for the Introduction to Data Science course for Portfolio Update #1.

The app demonstrates loading a CSV dataset and using Streamlit to build a data interface for exploring and filtering the data.

The dataset contains species, islands, and bill length & depth, among other metrics.

## Features

- This app displays a title and a short description 
- Loads the CSV file into a pandas DataFrame
- Shows the dataset in an interactive table
- Allows user to:
  - Filter penguins by species using a dropdown 
  - Filter penguins by bill depth using a slider (using decimal increments (float))

These interactive elements then update the dataframe 

## How to Run the App Locally

1. Ensure you have Python installed.
2. Install the necessary libraries using:
   ```bash
   pip install streamlit pandas
   ```
3. Navigate to the `basic_streamlit_app/` folder in your terminal.
4. Run the app using the command:
   ```bash
   streamlit run main.py
   ```

## Repository Structure

- `main.py`: The main Python script containing the Streamlit application code.
- `README.md`: This documentation file.
- `data/`: A directory containing the dataset (`.csv`) used by the app.
