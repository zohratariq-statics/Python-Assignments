
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    student_class = input("Enter class: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    students[roll_no] = {
        "name": name,
        "age": age,
        "class": student_class,
        "roll_number": roll_no,
        "marks": marks
    }

print("\nAll Student Records:")

for roll_no, details in students.items():
    print(roll_no, ":", details)
