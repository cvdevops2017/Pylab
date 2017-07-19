students = []

def get_student_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student["name"].title()
    return student_titlecase

def print_students_titlecase():
    students_titlecase = get_student_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file.")







student_list = get_student_titlecase()

student_name = input("Enter student name:") 
student_id = input("Enter student ID:")

add_student(student_name, student_id)
print_students_titlecase()


