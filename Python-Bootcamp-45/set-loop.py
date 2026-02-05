hobbies = [
    "football", "music", "reading", "reading", "reading", "music","music",
    "coding", "cleaning", "hokkey","hokkey","hokkey","hokkey","hokkey", "panda",
    "panda", "panda", "panda", "coding",
    "football", "gaming","gaming","gaming","gaming", "coding", "cleaning","cleaning","cleaning",
    "selling","selling","selling", "enjoying","enjoying","enjoying","enjoying","enjoying", "kidding", "joking","kidding", "joking","kidding", "joking"
]

unique_hobbies = set(hobbies)

# NECHTA UNIQUE HOBBY BOR
print(f"\nTotal unique hobbies: {len(unique_hobbies)}")

# UNIQUE HOBBIES (SET)
print("Unique hobbies:")
for hobby in unique_hobbies:
    print("-", hobby)

# HAR BIR HOBBY NECHA MARTA QAYTARILGAN
print("\nHobby counts:")

for hobby in unique_hobbies:
    count = 0
    for h in hobbies:
        if h == hobby:
            count += 1
    print(f"{hobby}: {count}")

# ENG KO‘P UCHRAGAN HOBBY

most_common = None
max_count = 0

for hobby in unique_hobbies:
    count = 0
    for h in hobbies:
        if h == hobby:
            count += 1

    if count > max_count:
        max_count = count
        most_common = hobby

print(f"\nMost common hobby: {most_common} ({max_count} times)")

min_count = max_count      # katta son bilan boshlanadi
least_common = None

for hobby in unique_hobbies:
    count = 0          # HAR SAFAR YANGI

    for h in hobbies:
        if h == hobby:
            count += 1

    if count < min_count:
        min_count = count
        least_common = hobby

print(f"Least common hobby: {least_common} ({min_count} times)")


# FAQAT BIR MARTA UCHRAGAN HOBBYLAR

print("\nHobbies used only once:")

for hobby in unique_hobbies:
    count = 0
    for h in hobbies:
        if h == hobby:
            count += 1

    if count == 1:
        print("-", hobby)
