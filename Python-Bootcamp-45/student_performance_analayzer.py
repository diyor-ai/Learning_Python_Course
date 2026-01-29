# Student Performance Analyzer

grades = [45, 78, 30, 90, 55, 100, 61, 20, 88]
# Task-1
total = 0
for grade in grades:
    total += grade

average = total / len(grades)
print(f"Average grade: {average}")

# Task-2
max_value = grades[0]

for grade in grades:
    if grade > max_value:
        max_value = grade

print(f"Maximum grade: {max_value}")

# Task-3-4
for index, value in enumerate(grades):
    if value >= 60:
        continue
    print(f"Index: {index}: {value} Failed")

# Task-5

while True:
    score = int(input("Enter your score: "))
    if score < 0 or score > 100:
        print(f"Your score is {score}. Please enter a valid score.")

    elif score <= 60:
        print(f"Your score is {score}. You are failed!!! ")
        break

    else:
        print(f"Your score is {score}. You are passed!!!")
        break

scores = [99, 98, 77, 96, 98, 58, 67, 68, 95,]

passed = []
not_passed = []

for index, value in enumerate(scores):
    if value >= 60:
        passed.append(value)
    elif value < 60:
        not_passed.append((index,value))


if not not_passed:
    print("All students passed!!!")
else:
    for ind , val in not_passed:
     print(f"INDEX: {ind}: {val} Failed")
