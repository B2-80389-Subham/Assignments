import pandas as pd

# Create a DataFrame for employee data
data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Salary": [50000, 55000, 60000, 62000, 58000, 63000, 65000, 67000, 70000, 72000]
}

employee_df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
employee_df.to_csv("employee_data.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt

# Read the employee data from the CSV file
employee_df = pd.read_csv("employee_data.csv")

# i) Line plot
plt.figure(figsize=(10, 6))
plt.plot(employee_df["EmployeeID"], employee_df["Salary"], marker='o', linestyle='-', color='b')
plt.title("Line Plot: Employee ID vs. Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.grid(True)

# Save the Line Plot as an image
plt.savefig("line_plot.png")

# ii) Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(employee_df["EmployeeID"], employee_df["Salary"], color='g')
plt.title("Bar Graph: Employee ID vs. Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.grid(axis='y')

# Save the Bar Graph as an image
plt.savefig("bar_graph.png")

# iii) Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(employee_df["EmployeeID"], employee_df["Salary"], color='r', marker='o')
plt.title("Scatter Plot: Employee ID vs. Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.grid(True)

# Save the Scatter Plot as an image
plt.savefig("scatter_plot.png")

# Show the plots
plt.show()
