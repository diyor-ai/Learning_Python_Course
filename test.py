data = [
    "football", "music", "reading", "music",
    "coding", "cleaning", "hokkey", "panda",
    "panda", "panda", "panda", "coding",
    "football", "gaming", "coding", "cleaning",
    "selling", "enjoying", "kidding", "joking"
]
print(f"Length of data: {len(data)}")

for d in data:
    print("-", d)


unique_data = set(data)
print(f"Unique data: {len(set(data))}")

for d in unique_data:
    print("-", d)

print("Hooby count:")
for x in unique_data:
    count =0
    for y in data:
        if x == y:
            count += 1
    print(f"{x} : {count}")