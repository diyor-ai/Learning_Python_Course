"""
1. Recursion Nima va Nega Kerak?
Rekursiya – function o'zini chaqirishi. Bu matematik va dasturlashda umumiy tushuncha,
masalan, data bo'yicha "tsikl" qilish uchun ishlatiladi.
Afzalliklar: Kodni qisqa va matematik jihatdan go'zal qiladi, lekin ehtiyot bo'ling – xato yozilsa,
 cheksiz tsikl (stack overflow) chiqadi yoki xotira/processor ko'p sarflaydi.
Nega esda qolarli? Rekursiya – "zinapoya pastga tushish" kabi:
Har qadamda o'zingizni pastga chaqirasiz, toki pastki (base case) gacha.
AI da nima uchun? AI'da rekursiya tree models (decision trees), search algorithms (DFS – Depth-First Search)
va optimization'da ishlatiladi. Masalan, neural net pruning (qirqish) yoki game AI (shaxmat harakatlari)."""


def cutdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        cutdown(n - 1)


cutdown(6)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(64))

"""
3. Fibonacci Sequence (Fibonachchi Ketma-ketligi)
Fibonachchi – klassik misol: Har son ikkita oldingi sonning yig'indisi (0, 1, 1, 2, 3, 5, 8, 13, ...)"""


def fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))  # Chiqadi: 13 (7-chi son)


# 4. Recursion with Lists (Ro'yxatlar Bilan Rekursiya)
# Rekursiya ro'yxatni elementma-element qayta ishlash uchun foydali.

def sum_mylist(num):
    if len(num) == 0:
        return 0
    else:
        return num[0] + sum_mylist(num[1:])


mylist = [1, 2, 3, 4, 5, 6]

print(sum_mylist(mylist))

def max_num(number):
    if len(number) == 1:
        return number[0]
    else:
        max_of_rest = max_num(number[1:])
        return number[0] if number[0] > max_of_rest else  max_of_rest

mylist2 = [3,5,2,5,34,6,46,66,2,46,6,77]
print(max_num(mylist2))

import sys
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())

#task o'rgangan narsalarimiz haqida

def reverse_list_print(lst):
    if len(lst) == 0:
        return None
    else:
        return lst

my_task = [1,2,3,4]

print(reverse_list_print(my_task))