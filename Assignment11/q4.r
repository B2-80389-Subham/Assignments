student_data <- data.frame(
  RollNo = c(1, 2, 3, 4, 5),
  StudentsName = c("Alice", "Bob", "Charlie", "David", "Eve"),
  Age = c(20, 22, 21, 23, 19),
  Score = c(85, 90, 78, 95, 88)
)

selected_data <- student_data[c(3, 5), c(1, 3)]
print(selected_data)
