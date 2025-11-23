# creating classes

class MyClass:
    x = 77


p1 = MyClass()

print(p1.x)

# You can delete objects by using the del keyword:
del p1

# Note: Each object is independent and has its own copy of the class properties.
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


class Person:
    pass


class Student:
        def __init__(self, name , age = 18 , major = "Undeclared"):
            self.name = name
            self.age = age
            self.major = major

p1 = Student("Saidjon", 20, "Soldier")
p2 = Student("Abbos")
p3 = Student("Diyor", 25, "AI Engineer")

print(f"Name: {p1.name}\nAge: {p1.age}\nMajor: {p1.major}")
print(f"Name: {p2.name}\nAge: {p2.age}\nMajor: {p2.major}")
print(f"Name: {p3.name}\nAge: {p3.age}\nMajor: {p3.major}")

""" 
print(f"Name: {p1.name}\n"
      f"Age: {p1.age}\n"
      f"Major: {p1.major}")
"""

