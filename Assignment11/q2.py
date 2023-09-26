import pandas as pd

# i) Read the dataset "Salaries.csv" into a DataFrame
df = pd.read_csv("Salaries.csv")

# ii) Display the first five records
print("First five records:")
print(df.head())

# iii) Display the first ten records
print("\nFirst ten records:")
print(df.head(10))

# iv) Display the last five records
print("\nLast five records:")
print(df.tail())

# v) Display the last ten records
print("\nLast ten records:")
print(df.tail(10))

# vi) Display the columns inside the dataset
print("\nColumns in the dataset:")
print(df.columns)

# vii) Display the shape of the data
print("\nShape of the data (rows, columns):", df.shape)

# viii) Describe the dataset
print("\nDescriptive Statistics:")
print(df.describe())

# ix) Display information about the dataset and analyze the data
print("\nDataset Information and Analysis:")
print(df.info())
# You can analyze data types, non-null counts, memory usage, etc., from the info() method output.

# x) Display the types of each column
print("\nData Types of Each Column:")
print(df.dtypes)
