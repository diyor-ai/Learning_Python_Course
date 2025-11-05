#1️⃣ lambda — qisqa funksiya
# lambda — bu nomi yo‘q funksiya (anonim funksiya), 1 qatorda yoziladi.

kv = lambda x: x ** 2
print(kv(3))

KV = lambda dior:print(f"salom {dior}")
print(KV("Said+"))

ismlar = lambda name: name + " welcome Ai engineer"
print(ismlar("Sattor"))

# map() — ro‘yxatdagi har bir elementga funksiya qo‘llash
#🧠 map() = "apply this function to every element"

sonlar = [1, 2, 3, 4, 5]

kv_sonlar = list(map(lambda x: x **2, sonlar))
print(kv_sonlar)

names = ["Diyor", "Said", "Malak"]
ism = list(map(lambda name:name + " welcome bro",names))
print(ism)


# filter() — faqat shartga mos elementlarni saqlaydi
#filter() → True qaytaradigan elementlargina qoladi.

raqamlar = [ 9,2,6,3,3,]
juftlar = list(filter(lambda x: x % 2 == 0 , raqamlar))
print(juftlar)

animals = ["wolf", "sheep", "Lion", "Cow", "Dog"]

Meat = list(filter(lambda x : len(x) >= 4 , animals))
print(Meat)

#4️⃣ reduce() — barcha elementlarni ketma-ket birlashtiradi
from functools import reduce

sonlar = [1, 2, 3, 4, 5]
yigindi = reduce(lambda x, y: x + y, sonlar)
print(yigindi)  # 15

pul = ["dollar", 'yuan', "so'm", "rubl", "pound"]
tekshir = reduce(lambda d, s: d + f"{s} bu valyuta!", pul)
print(tekshir)

#🧩 5️⃣ Ichki funksiya (Inner function)
#   Funksiya ichida boshqa funksiya yaratish mumkin.

def salom_ber(name):
    def ichki():
        return f"Salom, {name}!"
    return ichki()

print(salom_ber("Diyor"))

def ask_name(name):
    def ask_surname():
        return f"Your surname {name}"
    return ask_surname()

print(ask_name("Sattor"))