def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, 
    {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))
# TypeError: unsupported operand type(s) for +: 'int'
# and 'NoneType'

#   File "/Users/macos/Launch_School/py_101/lesson_2/average_grade.py", line 25, in <module>
#     print(average_grade(grades))
#           ^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/macos/Launch_School/py_101/lesson_2/average_grade.py", line 7, in average_grade
#     total = sum(grades)
#             ^^^^^^^^^^^
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'