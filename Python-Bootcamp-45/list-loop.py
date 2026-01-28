grades = [45, 78, 30, 90, 55, 100, 61]

for index, value in enumerate(grades):
    print(index, value)

total = 0

for grade in grades:
    total = total + grade

average = total / len(grades)
print(f"Average is {average}")

max_value = grades[0]

for grade in grades:
    if grade > max_value:
        max_value = grade

print(f"Maximum value is {max_value}")

for index, value in enumerate(grades):
    if value < 60:
        print(f"Index {index} : {value} FAILED")
