# Create a data frame for student information
student_data <- data.frame(
  RollNo = c(1, 2, 3, 4, 5),
  StudentsName = c("Alice", "Bob", "Charlie", "David", "Eve"),
  Age = c(20, 22, 21, 23, 19),
  Score = c(85, 90, 78, 95, 88)
)

# 1. Get the number of columns
num_columns <- ncol(student_data)
cat("Number of columns:", num_columns, "\n")

# 2. Get the number of rows
num_rows <- nrow(student_data)
cat("Number of rows:", num_rows, "\n")

# 3. Get the column names
column_names <- colnames(student_data)
cat("Column names:", column_names, "\n")

# 4. Get the first 3 rows
first_3_rows <- student_data[1:3, ]
cat("First 3 rows:\n")
print(first_3_rows)

# 5. Get the last 3 rows
last_3_rows <- student_data[(num_rows - 2):num_rows, ]
cat("Last 3 rows:\n")
print(last_3_rows)

# 6. Get general information
cat("General Information:\n")
str(student_data)

# 7. Get statistical information
cat("Statistical Information:\n")
summary(student_data)
