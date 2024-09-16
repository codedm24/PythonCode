#class
print('class 1')
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

print('class 2')
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"    
    
    def myfunc(self):
        print("Hello my name is " + self.name)

    def myfunc1(self):
        return f"Hello my name is {self.name}"

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)
p1.myfunc()
print(p1.myfunc1())

p1.name = "Michael"
print(p1)

del p1.age

del p1

print("class 3")

class Person:
    pass
