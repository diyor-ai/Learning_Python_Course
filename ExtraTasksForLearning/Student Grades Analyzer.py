# 🎯 Vazifa:
# Talabalar baholari ro‘yxati berilgan. Sizga:
# Har bir talabani o‘rtacha bahosini hisoblash
# Eng yaxshi talabani topish
# O‘rtacha bahosi 80 dan yuqori bo‘lgan talabalar sonini chiqaring

students = {
    "Vali": [88, 53, 86],
    "Said": [99, 84, 100],
    "Dior": [88, 99, 23],
    "Malak": [99.88, 98],
    "Sattor": [64, 34, 45]
}


for key, value in students.items():
    avarage = round(sum(value) / len(value), 2)
    print(f"{key} avarage: {avarage}")


for value in students.values():

    avarage1 = [sum(value) / len(value)]

    new_score = max(avarage1)

    print(f"max score {new_score}")





