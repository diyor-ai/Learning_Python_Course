students = (
    ("Ali", (78, 85, 90)),
    ("Vali", (55, 60, 58)),
    ("Hasan", (95, 92, 88)),
    ("Husan", (40, 45, 50))
)

for student in students:
    print(f"{student[0]} -> {student[1]}")

students_results = []
for student in students:
    total = 0
    for grade in student[1]:
        total += grade
    average = total / len(student[1])
    students_results.append((student[0], round(average, 2)))
    print(f"{student[0]} average: {average:.2f}")

for student in students_results:
    if student[1] >= 60:
        print(f"{student[0]} : Passed")
    else:
        print(f"{student[0]} : Failed")



top_student = students_results[0]
for x in students_results:
    if x[1] > top_student[1]:
        top_student = x
print(f"Top student: {top_student[0]} ({top_student[1]})")




failed_studets = []
passed_students = []
print("Failed students:")
for student in students_results:
    if student[1] < 60:
        failed_studets.append(student)
        print(student[0])
    else:
        passed_students.append(student)

print(f"Total : {len(students)}")
print(f"Passed : {len(passed_students)}")
print(f"Failed: {len(failed_studets)}")
