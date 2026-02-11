# Project => User Info Printer

users = {
    "user1": {
        "name": "Sali",
        "age": 22,
        "skills": ["python", "sql", "ai"],
        "active": True
    },
    "user2": {
        "name": "Vali",
        "age": 19,
        "skills": ["html", "css"],
        "active": False
    }
}

for key, value in users.items():
    print(f"USER: {key}")
    print(f"NAME: {value['name']}")
    print(f"AGE: {value['age']}")
    print(f"SKILLS: ")
    for skill in value['skills']:
        print(f" - {skill}")

    if value['active'] is True:
        print(f"Status: Active")
    else:
        print(f"Status: Inactive")


    if value['active'] is True:
        print(f"Status: Active")
    else:
        print(f"Status: Inactive")