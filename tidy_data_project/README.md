# 🏅 2008 Olympic Medalists: Tidy Data Project

## 📖 Project Overview
In this project, I took a messy dataset of the 2008 Olympic Medalists and cleaned it up so it is easier to read, understand, and chart. 
I used the **Tidy Data Principles** to organize everything. Tidy Data basically has three simple rules:
1. Every variable gets its own column (like putting Gender in one column and Sport in another).
2. Every observation gets its own row (so each row is just ONE medal won).
3. Every value gets its own cell. 
By reorganizing the data this way, we can quickly make charts and count up totals!

## 📊 Dataset Description
The data I started with is from a file called `olympics_08_medalists.csv`. 
**The Problem:** The original data was messy because the column names had too much information squished together (like `"Men_100m"`). The actual medals were also scattered all over the place.
**How I Cleaned the Data:**
* **Melting:** I grouped the scattered data into a single column so it was easier to work with.
* **Splitting:** I broke apart those squished column names at the underscore `_` to give `Gender` and `Sport` their own separate columns.
* **Text Formatting:** I cleaned up weird spacing, removed remaining underscores, and capitalized the words so everything looks neat.
* **Counting:** I added a `Count` column with a value of `1` for every row, which makes it super easy to add up how many medals each sport got.

## 🚀 Instructions
**What You Need:**
To run this code, you will need Python and Jupyter Notebook installed, along with two specific packages:
* `pandas` (for organizing the data)
* `matplotlib` (for drawing the charts)
You can install these in your terminal by typing:
`pip install pandas matplotlib jupyter`
**How to Run the Code:**
1. Download this project folder to your computer.
2. Make sure the `olympics_08_medalists.csv` file is inside a folder named `/Data/`.
3. Open your terminal, go to the folder, and type `jupyter notebook` to launch it.
4. Open the notebook file and run the steps from top to bottom!






