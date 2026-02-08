import streamlit as st
import pandas as pd

st.title("Basic Streamlit App")

st.write("""This Streamlit app demonstrates how to load a CSV file, 
         display it as a DataFrame, and apply simple interactive filters.""")

df = pd.read_csv("data/penguins.csv")

st.write("Here's our data:")
st.dataframe(df)


st.subheader("Use filters to sort the data!")

# Filter by Species
species = st.selectbox("Select a species of Penguin", df["species"].unique())
filtered_df = df[df["species"] == species]

st.write(f"Penguins of that species {species}:")
st.dataframe(filtered_df)

#Filter by Bill Depth
depth = st.slider("Slide me to filter by bill depth", 
                  float(df["bill_depth_mm"].min()), 
                  max_value=float(df["bill_depth_mm"].max()),
                  step = 0.1)

filtered_df = df[df["bill_depth_mm"] == depth]

st.write(f"Penguins with bill depths of {depth}: ")
st.dataframe(filtered_df)

st.subheader("Summary Statistics")
st.write(df.describe())