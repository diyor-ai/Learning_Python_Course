def greet():
    print("Hello Diyor")


greet()
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# "return" is in python

def greeting():
    return "Bro , keep going, do not give up!!!!"


# print(greeting())
greeting()


def say_hello(fname):
    print(f"Hello Mr{fname}")


hello = say_hello("Diyor")
print(hello)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


def kitob_ifno(nomi, sahifa=100):
    return f"Kitob: {nomi}, Sahifa: {sahifa}"


print(kitob_ifno("Python"))
print(kitob_ifno("Ai", 200))


def add(a, b):
    print(a + b)


result = add(2, 3)
print(result)  # avval 5 chiqadi, so‘ng None


def UserInfo():
    name = "Diyor"
    age = "23"
    return name, age


n, a = UserInfo()
print(n, a)


def checkAge(age):
    if age >= 18:
        print("Kirish mumkin")


checkAge(18)


def get_name(name):
    return f"Salom Senga {name} AI Engineer"


def kvadrat(x):
    return x * x

kv = kvadrat(6)
print(kv)

def urtacha(a, b , c):
    print((a + b + c) / 3)

urtacha(8,2, 5)


def farq_print(name):
    print(name)

farq_print("Said")

def farq_print2(name):
    return name

said = farq_print("Said")

print(said)
