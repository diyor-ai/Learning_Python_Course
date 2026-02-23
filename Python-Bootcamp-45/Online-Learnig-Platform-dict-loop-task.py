academy = {
    "Backend": {
        "Python": {
            "Ali": {
                "completed": True,
                "scores": [85, 90, 88]
            },
            "Vali": {
                "completed": False,
                "scores": [70, 75]
            }
        },
        "Django": {
            "Ali": {
                "completed": True,
                "scores": [80, 82]
            }
        }
    },
    "Frontend": {
        "React": {
            "Sami": {
                "completed": True,
                "scores": [90, 92, 95]
            }
        }
    }
}

"""
Ali
Courses: 2
Total score: 425
Average score: 85.0
------------------
"""

student_stats = {}
for direction in academy.values():
    for course in direction.values():
        for student, info in course.items():
            if student not in student_stats:
                student_stats[student] = {
                    "courses": 0,
                    "total_score": 0,
                    "score_count": 0
                }
            student_stats[student]["courses"] += 1
            student_stats[student]["total_score"] += sum(info["scores"])
            student_stats[student]["score_count"] += len(info["scores"])

students_rate = []
for student, data in student_stats.items():
    average = data["total_score"] / data["score_count"]
    print(student)
    print("Courses:", data["courses"])
    print("Total score:", data["total_score"])
    print("Average:", round(average, 2))
    print("-------------")
    students_rate.append([student, round(average, 2)])

"""
Python
Students: 2
Completed: 1
"""

course_stats = {}
for direction in academy.values():
    for course, info in direction.items():
        if course not in course_stats:
            course_stats[course] = {
                "students": 0,
                "completed": 0,
            }
        for student, infoes in info.items():
            course_stats[course]["students"] += 1
            if infoes["completed"]:
                course_stats[course]["completed"] += 1

for course, data in course_stats.items():
    print(course)
    print("Students:", data["students"])
    print("Completed:", data["completed"])
    print("__" * 8)

# Top student: Sami (92.33)
top_student = students_rate[0]

for student in students_rate:
    if student[1] > top_student[1]:
        top_student = student
print(f"Top student: {top_student[0]} ({top_student[1]})")
print("__" * 8)

"""
Backend -> 2 students
Frontend -> 1 student
"""

course_type = {}
for direction, info in academy.items():
    course_type[direction] = {
        "student": 0
    }
    for course in info.values():
        for val in course.values():
            course_type[direction]["student"] += 1

for course, info in course_type.items():
    print(f"{course} -> {info['student']}")
