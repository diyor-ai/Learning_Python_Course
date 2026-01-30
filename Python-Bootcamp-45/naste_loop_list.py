"""
SENGA TOPSHIRIQ:

1️⃣ Barcha elementlar yig‘indisini top
2️⃣ Eng katta elementni top
3️⃣ Faqat toq sonlarni chiqar
4️⃣ Har bir qator yig‘indisini chiqar
5️⃣ (BONUS) Eng katta element qaysi indexda ekanini top

❗ List comprehension YO‘Q
❗ Faqat for, if, nested loop
"""

matrix = [
    [3, 7, 1],
    [8, 4, 2],
    [6, 9, 5]
]
total = 0
for i in matrix:
    for j in i:
        total += j
print(f"Total addition of matrix is {total}")

max_val = matrix[0][0]

for x in matrix:
    for y in x:
        if y > max_val:
            max_val = y
print(f"Max value of matrix is {max_val}")

odd_number = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] % 2 != 0:
            odd_number.append(matrix[row][col])
print(f"Odd numbers are {odd_number}")

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(col)