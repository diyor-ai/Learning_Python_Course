platform = {
    "user1": {
        "name": "Ali",
        "age": 20,
        "interests": {"python", "ai", "football"},
        "books": {
            "book1": {"title": "AI Basics", "pages": 300},
            "book2": {"title": "Python Pro", "pages": 250}
        }
    },
    "user2": {
        "name": "Vali",
        "age": 22,
        "interests": {"python", "gaming", "music"},
        "books": {
            "book1": {"title": "Clean Code", "pages": 400}
        }
    },
    "user3": {
        "name": "Sami",
        "age": 19,
        "interests": {"ai", "music"},
        "books": {}
    }
}

"""
Task-1

USER: Ali
Interests count: 3
Books count: 2
Total pages: 550
------------

"""
for user_id, info in platform.items():
    print(f"User: {info["name"]}")
    print(f"Interests count: {len(info["interests"])}")
    print(f"Books count: {len(info["books"])}")
    # print(f"Total pages: {info["books"]["pages"]}")
    total_pages = 0
    for book in info["books"].values():
        total_pages += book["pages"]
    print(f"Total pages: {total_pages}")
    print("-" * 16)

"""
Task-2

All interests:
{'python', 'ai', 'football', 'gaming', 'music'}

At least 2 users:
{'python', 'ai', 'music'}

Only 1 user:
{'football', 'gaming'}

"""
interests = []

for value in platform.values():
    interests.extend(value["interests"])
print(f"ALL Interests:\n{set(interests)}")

at_least_two = set(platform["user1"]["interests"] & platform["user2"]["interests"] | platform["user1"]["interests"] &
                   platform["user3"]["interests"] | platform["user2"]["interests"] & platform["user2"]["interests"] &
                   platform["user3"]["interests"])
print(f"At least two users:\n{at_least_two}")

set_interest = set(interests)
only_one = set_interest - at_least_two
print(f"Only one user:\n{only_one}")

"""
Task-3

Platform total pages: 950

Average pages per user: 316.67

Average pages per user: 316.67

"""

Total_pages = 0

for book
