i = 0
while i < 7:
    print(i)
    i += 1
    if i == 5:
        continue
else:
    print("i is no longer less than 7")

"""urinish = 3
while urinish > 0:
    parol so‘ra
    agar to‘g‘ri bo‘lsa:
        ruxsat ber
        break
    aks holda:
        urinishni kamaytir
agar urinish tugasa:
    rad et"""

password = "python123"
x = 3
while x > 0:
    answer = input(f"What is password? ")
    if password == answer:
        print(f"Your passoword is True.")
        break
    x -= 1
    print(f"{answer} is False.")
    if x == 0:
        break
        print("Access Denied")
