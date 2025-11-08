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

avarages = {}

for key, value in students.items():
    avg = sum(value) / len(value)
    avarages[key] = avg
    print(f"{key} avarage: {avg:.2f}")


top_student = max(avarages, key=avarages.get)

print(f"\nTop student: {top_student} ({avarages[top_student]:.2f})")

if avarages > 50:
    print(len(avarages))