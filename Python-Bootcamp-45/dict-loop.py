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

# Second version
print("-" * 64)

for user_id, info in users.items():
    print(f"\nUSER: {user_id}")
    for key, value in info.items():
        if isinstance(value, list):
            print(f"{key.upper()}:")
            for item in value:
                print(f" - {item}")
        elif isinstance(value, bool):
            status = "Active" if value else "Inactive"
            print(f"Status: {status}")
        else:
            print(f"{key.upper()}: {value}")

    print("-" * 16)

# Create the dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 2024}

# Print the model
print(car["model"])

# Change the year to 2025
car["year"] = 2025

# Add a color key
car["color"] = "red"

# Remove the brand key
car.pop("brand")

# Print the dictionary
print(car)
