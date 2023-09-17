def student_data(student_id, **kwargs):
    # Print the student ID
    print(f"Student ID: {student_id}")

    # Check if student_name is provided in kwargs
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    # Check if student_class is provided in kwargs
    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}\n")


# Example usage:
student_data(101)  # Only student ID provided
student_data(102, student_name="saurabh")  # Student ID and name provided
student_data(103, student_class="Grade 10")  # Student ID and class provided
student_data(104, student_name="sambit", student_class="Grade 11")  # Student ID, name, and class provided
