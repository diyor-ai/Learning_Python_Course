def hisobla(a, b):
    qosh = a + b
    kopaytir = a * b
    return qosh, kopaytir

x, y = hisobla(3 , 5)

print("Yig'indi: ", y)



#  *args — noma’lum miqdordagi argumentlar
#Agar oldindan nechta parametr bo‘lishini bilmasang — *args ishlat.

def urtacha_hisobla(*sonlar):
    return sum(sonlar) / len(sonlar)

print(urtacha_hisobla(3,8,4))

def user_info(**user):
    for key , value in user.items():
        print(f"{key} : {value}")

user_info(ism="diyor", age=25,job= "Ai Enginner")


def kvadrar(x):
    return x * x

def ishlat(function , value):
    return function(value)

result = ishlat(kvadrar, 3)
print(result)

#homeworks

#1️⃣ hisobla() funksiyasi tuz:
#har qanday sonlar ro‘yxatini olsin (*args)
#yig‘indi, o‘rtacha, eng katta va eng kichik qiymatni qaytarsin (4 ta qiymat return qilsin)

def hisobla(*n):
    yigindi = sum(n)
    urtacha = sum(n) / len(n)
    eng_katta = max(n)
    eng_kichik = min(n)
    return yigindi, urtacha, eng_katta, eng_kichik

a , b , c , d = hisobla(35, 32, 43, 31 , 523 , 1)

print("Yig'indi:", a)
print("O'rtacha:", b)
print("Eng katta:", c)
print("Eng kichik:", d)

#foydalanuvchi_info(**kwargs) yoz:
#foydalanuvchi haqida ism, yosh, kasb kabi ma’lumotlarni chiqaradi.

def foydalanuchi_info(**info):
    for key , value in info.items():
        return f"{key} : {value}"

print(foydalanuchi_info(ism="Abbos", age=25 ,job="AI Engineer"))

#apply_function(func, value) yoz:
#func nomli boshqa funksiya va qiymat qabul qiladi.
#Misol: apply_function(abs, -5) → 5

def add(q):
    return q * 2

def apply_function(func, value):
    return func(value)

natija = apply_function(add, 15)
print(natija)

# 4Global va local o‘zgaruvchi farqini ko‘rsatadigan kichik misol yoz.

x = "Global"
def farqlash():
    x = "local"
    print(x) #natija local

farqlash()
print(x) #natija Global
