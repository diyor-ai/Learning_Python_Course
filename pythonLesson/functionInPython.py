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

#print(greeting())
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