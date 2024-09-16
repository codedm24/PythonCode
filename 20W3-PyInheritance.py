#Inheritance
print("class 1")

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, " ", self.lname)

x = Person("John", "Collins")
x.printname()

print("class 2")

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self,fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome",self.fname, self.lname," to the class of ", self.graduationyear)

    def functionWithoutSelf(self):
        print("Cannot declare Function without self inside a class")    

x = Student("Mike", "Olsen",2019)  
x.printname()    
x.welcome()  
x.functionWithoutSelf()
