import sys

a = [1, 2, 3]
b = a
b.append(4)

print(b)
print(f"a va b : {a is b}")
print(f"a va b : {a == b}")
# Savol: a nima bo'ladi? Nega? id(a) va id(b) ni tekshir.
print(type(a))
print(sys.getsizeof(a))
print(sys.getsizeof(b))
"""
Javoblar:
a bu list.
"""
