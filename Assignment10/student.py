class Student:
    def __init__(self, rollno, studentName, course):
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = {}

    def __str__(self):
        return f"Roll No: {self.rollno}\nStudent Name: {self.studentName}\nCourse: {self.course}\nMarks: {self.marks}"

    def accept_student_data(self):
        self.rollno = input("Enter Roll No: ")
        self.studentName = input("Enter Student Name: ")
        self.course = input("Enter Course: ")
        self.accept_marks()

    def accept_marks(self):
        print("Enter marks for 5 subjects:")
        for i in range(5):
            subject_name = input(f"Enter subject {i+1} name: ")
            marks = float(input(f"Enter marks for {subject_name}: "))
            self.marks[subject_name] = marks

    def print_student_data(self):
        print("\nStudent Data:")
        print(self)


students = []
for i in range(5):
    print(f"Enter data for Student {i+1}:")
    student = Student(None, None, None)
    student.accept_student_data()
    students.append(student)

for i, student in enumerate(students):
    print(f"\nStudent {i+1} Details:")
    student.print_student_data()
