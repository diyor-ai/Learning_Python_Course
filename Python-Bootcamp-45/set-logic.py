user1 = {"football", "music", "coding", "reading"}
user2 = {"music", "coding", "gaming"}

common = user1 | user2

all_interests = user1 & user2

only_user1 = user1 - user2

only_user2 = user2 - user1

print("Common:", common)
print("All:", all_interests)
print("Only user1:", only_user1)
print("Only user2:", only_user2)
