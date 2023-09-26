import pandas as pd

# i) Read the dataset "Advertising.csv" into a DataFrame
df = pd.read_csv("Advertising.csv")

# ii) Print the first five records of the dataset
print("First five records:")
print(df.head())

# iii) Print the last five records from the dataset
print("\nLast five records:")
print(df.tail())

# iv) Display the columns inside the dataset
print("\nColumns in the dataset:")
print(df.columns)

# v) Display the last three records from the dataset
print("\nLast three records:")
print(df.tail(3))

# vi) Display information about the dataset and analyze the data
print("\nDataset Information and Analysis:")
print(df.info())
# You can analyze data statistics, data types, and memory usage from the info() method output.

# vii) Display types of each column
print("\nData Types of Each Column:")
print(df.dtypes)

# viii) Check for null values in the dataset and display the sum of null values inside each column
print("\nNull Values in Each Column:")
print(df.isnull().sum())

# ix) Drop the 'radio' column from the dataset and display the first ten records
df.drop('radio', axis=1, inplace=True)
print("\nAfter dropping 'radio' column, the first ten records:")
print(df.head(10))

# x) Increase the 'sales' by 10% and add a new column "updated_sales" in the DataFrame
df['updated_sales'] = df['sales'] * 1.10

# xi) Display the shape of the data
print("\nShape of the data (rows, columns):", df.shape)

# xiii) Describe the dataset
print("\nDescriptive Statistics:")
print(df.describe())
