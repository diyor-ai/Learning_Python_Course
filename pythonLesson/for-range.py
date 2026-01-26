import random

from faker import Faker

fake = Faker()


def students():
    students_list = []
    for i in range(100):
        students_list.append(fake.name())
    return students_list


def grade():
    grades_list = []
    for i in range(100):
        grades_list.append(random.randint(1, 100))
    return grades_list


new_students = students()
new_grades = grade()

def student_grade():
    student_grades_dict = {}
    for s, g in zip(new_students, new_grades):
        student_grades_dict[s] = g
    return student_grades_dict

student_grades_dict = student_grade()


def even_num():
    even = []
    for i in range(2, 100, 2):
        even.append(i)
    return even


new_even_num = even_num()
print(new_even_num)


def odd_num():
    total = 0
    for i in range(1, 100, 2):
        total += i
    return total


new_odd_num = odd_num()
print(new_odd_num)

nums = [3, 7, 2, 9, 5]

max_num = nums[0]

for x in nums:
    if x > max_num:
        max_num = x

print(max_num)


