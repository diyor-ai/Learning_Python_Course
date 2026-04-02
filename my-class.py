"""" # Given strings
s1 = "Abc"
s2 = "Xyz"

# Reverse the second string
s2_rev = s2[::-1]

# Initialize result and get max length
result = ""
max_len = max(len(s1), len(s2))

# Build the result string
for i in range(max_len):
    if i < len(s1):
        result += s1[i]
    if i < len(s2_rev):
        result += s2_rev[i]

print(result)

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# Convert both to lowercase and count
count = str1.lower().count(sub_string.lower())

print("The USA count is:", count)



input_str = "PYnative29@#8496"
total = 0
cnt = 0

for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

avg = total / cnt
print("Sum:", total, "Avg:", avg)

str1 = "PYnative"

# Step: Slice with step -1 to reverse
str1 = str1[::-1]

print("Reversed:", str1)

str1 = "PYnative"

# Step: Join the reversed iterator
str1 = ''.join(reversed(str1))

print("Reversed:", str1)


str1 = "Emma is a data scientist who knows Python . Emma works at google"

#use rfind() = to find from right

last_occurrenct = str1.rfind("Emma")

print(f"Last occurence starts at index {last_occurrenct}")

"""
str1 = "Emma-is-a-data-scientist"
result = str1.split('-')
print(result)