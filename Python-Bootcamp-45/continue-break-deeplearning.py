for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(1, 51):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

skipped = []
printed = []

for i in range(1,51):
    if i % 3 == 0 or i % 5 == 0:
        skipped.append(i)
        continue
    printed.append(i)

print(f"skipped: {skipped}")
print(f"printed: {printed}")

