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

#Decorator With Arguments (Dekoratorning O'z Argumentlari)

def change_dec_arg(n):
    def decorator(func):
        def myinner():
            if n == 1:
                return func().lower()
            else:
                return func().upper
        return myinner
    return decorator

@change_dec_arg(2)
def myfunction():
    return "Hello Salim"

print(myfunction())