# Tidy Data Project: 2008 Olympic Medalists

## Project Overview
This project demonstrates how to clean and reshape a messy dataset using tidy data principles in Python. 
The dataset contains information about medalists from the 2008 Olympics, 
but it is originally structured in a wide format where multiple variables are combined into column names.

The goal of this project is to transform the dataset so that:
- each variable has its own column  
- each observation has its own row  
- the data is organized in a way that makes analysis easier  

After cleaning the data, I use pivot tables and visualizations to explore patterns in medal distributions 
across sports and genders.

---

## What is Tidy Data?
Tidy data is a way of structuring datasets so they are easier to work with. According to Hadley Wickham’s 
tidy data principles:
- each variable should be in its own column  
- each observation should be in its own row  
- each type of observational unit should be in its own table  

Using tidy data makes it much easier to perform analysis, create visualizations, and apply functions in pandas.


## Dataset Description
- ##Dataset:** 2008 Olympic Medalists  
- **Source:** https://edjnet.github.io/OlympicsGoNUTS/2008/  

### Original Structure
The dataset is in a wide format:
- rows represent athletes  
- columns represent combinations of **gender + sport** 
- cell values contain medal types 

### Pre-processing Steps
To clean the dataset:
1. Used `melt()` to convert the data from wide to long format  
2. Removed missing values (since most cells are empty)  
3. Used `str.split()` to separate combined variables (`gender` and `sport`)  
4. Used `str.replace()` to clean text values  
5. Selected only relevant columns for the final tidy dataset


### Dependencies
To run this notebook, make sure the following Python libraries are installed:
- pandas  
- matplotlib  
- jupyter  


## Instructions

### Step 1: Install the required libraries 

### Step 2: Open notebook and make sure data set is in the correct place

### Step 3: Run the entire notebook

### Step 4: Review output

### Links
Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
Tidy Data Paper: https://vita.had.co.nz/papers/tidy-data.pdf
Dataset Source: https://edjnet.github.io/OlympicsGoNUTS/2008/





