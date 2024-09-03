x = 5
y = "John"
print(x)
print(y)

x = 4 # x is of type int
x = "Sally" # x is of type str
print(x)

x = str(3) # x will be 3
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

x = "John"
#is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#legal variable name
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "JOHN"
myvar2 = "JOHN"

#Illegal variable name
#2myvar = "John"
#my-var = "John"
#my var = "John"

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#snake case
my_variable_name = "John"

#assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assign one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack list, tuple
fruits = ["apple","banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

x = 5
y = 10
print(x + y)

#Error condition - type mismatch when using + with two different type of variables
x = 5
y = "John"
#print(x + y)

# This will work - comma seperator accepts different type of variables
print(x, y)

#global can be used inside and outside a function
x = "awesome"

def myFunc():
    print("Pyhton is", x)

myFunc()

# variable with same name can only be used inside the function
def myFunc1():
    x = "fantastic"
    print("Python is " + x)

myFunc1()

print("Python is " + x)

# define a global variable inside a function
def myFunc2():
    global x 
    x = "fantastic"

myFunc2()

print("Python is " + x)

