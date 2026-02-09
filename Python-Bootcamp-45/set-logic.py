user1 = {"football", "music", "coding", "reading"}
user2 = {"music", "coding", "gaming"}

common = user1 & user2

all_interests = user1 | user2

only_user1 = user1 - user2

only_user2 = user2 - user1

print("Common:", common)
print("All:", all_interests)
print("Only user1:", only_user1)
print("Only user2:", only_user2)

# Task-2

Sali = {"football", "music", "coding", "reading"}
Vali = {"music", "coding", "gaming"}
Tali = {"coding", "swimming", "cleaning"}

all_interests2 = Sali & Vali & Tali

print(f"Umumiy Qiziqishlar: {all_interests2}")

# only Sali

only_Sali = Sali - Vali - Tali
print(f"Only Sali Qiziqishlar: {only_Sali}")

# only Vali

only_vali = Vali - Sali - Tali
print(f"Only Vali Qiziqishlar: {only_vali}")

# only Tali

only_Tali = Tali - Sali - Vali
print(f"Only Tali Qiziqishlar: {only_Tali}")

all_interests = Sali | Vali | Tali

print(f"All Qiziqishlar: {all_interests}")

at_least_two = (Sali & Vali) | (Sali & Tali) | (Vali & Tali)
only_one = all_interests - at_least_two
print("At least two users:", at_least_two)
print("Only one user:", only_one)

