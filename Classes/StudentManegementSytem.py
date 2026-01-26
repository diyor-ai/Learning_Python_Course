class Student:
    def __init__(self, name, age, major, grades):
        self.name = name
        self.age = age
        self.major = major
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return (f"Student: {self.name}, Age : {self.age}, Major: {self.major} "
                f"Grades: {self.grades}, Avarage Grades: {self.average_grade():2f}")


# 1. Talaba obyektlarini yaratish (Ma'lumotlar tuzilmasi)
student1 = Student("Ali Valiyev", 20, "AI Enginner", [85, 90, 78, 92])
student2 = Student("Gulshoda Karimova", 21, "Dizayn", [95, 88, 91])
student3 = Student("Farhod Aliyev", 19, "Economic", [70, 75, 80, 68])

student_list = [student1, student2, student3]

print("--Students List")

for student in student_list:
    print(student)

print("\n--- Spesific student ---")
print(f"{student1.name} ==>> Avarage Grade: {student1.average_grade():.2f}")


