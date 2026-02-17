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
    print(f"User: {info['name']}")
    print(f"Interests count: {len(info['interests'])}")
    print(f"Books count: {len(info['books'])}")
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
                   platform["user3"]["interests"] | platform["user2"]["interests"] & platform["user3"]["interests"])
print(f"At least two users:\n{at_least_two}")

set_interest = set(interests)
only_one = set_interest - at_least_two
print(f"Only one user:\n{only_one}")
print("-" * 26)

"""
Task-3

Platform total pages: 950

Average pages per user: 316.67

Top reader: Ali (550 pages)

"""

Total_pages = 0
average_pages_per_user = 0
user_total_pages = 0

for user, book in platform.items():
    for value in book["books"].values():
        Total_pages += value["pages"]
    average_pages_per_user = Total_pages / len(platform)
    for x in book["books"].values():
        user_total_pages += x["pages"]

print(f"Platform total pages: {Total_pages}")
print(f"Average pages per user: {average_pages_per_user}")

readers = []


def reader():
    for user, value in platform.items():
        total_pages = 0
        for book in value["books"].values():
            total_pages += book["pages"]
        readers.append([value["name"], total_pages])
    return readers


reader()

top_reader = readers[0]
for x in readers:
    if x[1] > top_reader[1]:
        top_reader = x
print(f"Top reader: {top_reader[0]} ({top_reader[1]} pages)")
