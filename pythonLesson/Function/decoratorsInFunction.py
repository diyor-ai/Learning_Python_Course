def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello Diyor"


@changecase
def diyor():
    return "I am AI Engineer"


print(myfunction())
print(diyor())


# Arguments in the Decorated Function
def changecaseer1(func):
    def myinner(x):
        return func(x).upper()

    return myinner


@changecaseer1
def fuc_decorator(name):
    return "Merhaba " + name


print(fuc_decorator("Diyor"))


# *args and **kwargs (Universal Argumentlar)
# Agar function argumentlari noma'lum bo'lsa, *args (tuple) va **kwargs (dict) ishlatiladi.

def my_arg_kwarg_func(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return myinner


@my_arg_kwarg_func
def myfunction(name):
    return "Hello " + name


print(myfunction("Sattor"))


# Decorator With Arguments (Dekoratorning O'z Argumentlari)

def change_dec_arg(n):
    def decorator(func):
        def myinner():
            if n == 1:
                return func().lower()
            else:
                return func().upper()

        return myinner

    return decorator


@change_dec_arg(15)
def myfunction():
    return "Hello Salim"


print(myfunction())


# 7. Multiple Decorators (Bir Necha Dekorator)
# Bir functionga ko'p decorator qo'llash mumkin – ular teskari tartibda ishlaydi (eng pastdagidan boshlab).


def uzgartir(func):
    def myinner():
        return func().upper()

    return myinner


def say_hello(func):
    def myinner():
        return "Salom " + func() + " Have a nice day"

    return myinner


@uzgartir
@say_hello
def my__function():
    return "Axror"

print(my__function())

#8. Preserving Function Metadata (Metadata Saqlash)
#Oddiy decorator'da asl function nomi yo'qoladi – functools.wraps bilan saqlash mumkin.

#example 1 (Yo'qolgan metadata)

def my_metadata(func):
    def myinner():
        return func().upper()
    return myinner

@my_metadata
def myfunction():
    return "Xayrli kun sizlarga xurmatli 'Coderlar'"

print(myfunction.__name__)

# True example

import functools

def my_changecase_metadata(func):
    @functools.wraps(func)
    def myinner():
        return func().lower()
    return myinner

@my_changecase_metadata
def myNameIsDiyor():
    return "Xayrli kech sizga AI Enginner"

print(myNameIsDiyor.__name__)
