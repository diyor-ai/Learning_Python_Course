i = 0
while i < 7:
    print(i)
    i += 1
    if i == 5:
        continue
else:
    print("i is no longer less than 7")

# password = "python123"
# attempts = 3
#
# while attempts > 0:
#     answer = input("What is password? ")
#
#     if answer == password:
#         print("Access Granted ✅")
#         break
#     else:
#         attempts -= 1
#         print(f"Wrong password ❌. Attempts left: {attempts}")
#
# else:
#     print("Access Denied 🔒")

PASSWORD = "python123"
MAX_ATTEMPTS = 3

attempt = 1

while attempt <= MAX_ATTEMPTS:
    answer = input("What is password? ")

    if answer == PASSWORD:
        print(f"Access Granted ✅ on attempt {attempt}")
        break
    else:
        print(f"Wrong password ❌. Attempts left: {MAX_ATTEMPTS - attempt}")
        attempt += 1
else:
    print("Access Denied 🔒")
