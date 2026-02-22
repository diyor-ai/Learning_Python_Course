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

for student, data in student_stats.items():
    average = data["total_score"] / data["score_count"]
    print(student)
    print("Courses:", data["courses"])
    print("Total score:", data["total_score"])
    print("Average:", round(average, 2))
    print("-------------")

"""
Python
Students: 2
Completed: 1
"""

course_stats = {}
for direction in academy.values():
    for course in direction.values():
        for student, info in course.items():
            if student not in course_stats:
                course_stats[student] = {
                    "students": 0,
                    "completed": False,
                }