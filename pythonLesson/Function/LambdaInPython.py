""""
Lambda Functions Nima va Sintaksisi
Lambda – anonim (nomsiz) function, ko'pincha bir martalik ish uchun ishlatiladi.
Sintaksis:lambda arguments : expression (natija avto qaytariladi).
Nega esda qolarli? Lambda – "qisqa telegramma" kabi: Argumentlarni olib, bitta ifodani bajaradi va natijani jo'natadi.
Argumentlar: Har qancha bo'lishi mumkin, lekin ifoda faqat bitta."""

x = lambda a: a + 12
print(x(5))

"""2. Nega Lambda Funksiyalarini Ishlatamiz?
Lambda ko'pincha boshqa function ichida ishlatiladi – bu uning kuchli tomoni.
Misol (Boshqa function ichida):
Bir function argumentini o'zgartirish uchun lambda qaytaradi."""


def my_func(f):
    return lambda a: a * f


my_doubler = my_func(2)
print(my_doubler(11))

my_tripler = my_func(3)
print(my_tripler(11))

""""
3. Lambda with Built-in Functions 
(Tayyor Funksiyalar Bilan)Lambda ko'pincha map(), filter(), sorted() bilan ishlatiladi –
 bu data bilan ishlashni tezlashtiradi.
map() bilan: Har elementga lambda qo'llaydi.
"""

# map() bilan har bir elemantga lambda qo'llaydi
numbers = [1, 2, 3, 4]
double = list(map(lambda q: q * 2, numbers))
print(numbers)
print(double)

# filter() bilan , shartga mos elementalrni tanlaydi

num = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = list(filter(lambda k: k % 2 != 0, num))
print(num)
print(odd_numbers)

# sorted() bilan: Custom tartiblash uchun key=lambda.

student = [("Diyor", 25), ("Saidbek", 11), ("Abbos", 18)]
sorted_student = sorted(student, key=lambda b: b[1])

print(student)
print(sorted_student)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])  # Ikkinchi element bo'yicha
print(sorted_students)  # Chiqadi: [('Tobias', 22), ('Emil', 25), ('Linus', 28)]

""""Task: Lambda bilan Data Filtering
Ro'yxat data = [10, -5, 20, -3, 15, 0] dan faqat musbat sonlarni tanlab, ularni kvadrat qilib yangi ro'yxat qaytaring (filter + map + lambda bilan).
Qo'shimcha: Natijani sorted bilan kichikdan kattaga tartiblang (key=lambda x: x).
Sinov: Print natijani."""

data = [10, -5, 20, -3, 15, 0]
new_data = list(filter(lambda x: x > 0,data))
new_squre = list(map(lambda x: x * x, new_data))
new_sorted = list(sorted(new_squre, key=lambda x: x))
print(new_sorted)
