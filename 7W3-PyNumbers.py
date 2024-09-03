x = 1 #int
y = 2.8 #float
z = 1j #complex
print("Type:",type(x),"Value:",x)
print("Type:",type(y),"Value:",y)
print("Type:",type(z),"Va;ue:",z)

#int type postive, negative
x = 1
y = 35656222554887711
z = -3255522
print(type(x), x)
print(type(y), y)
print(type(z), z)

#float ype positive, negative
x = 1.10
y = 1.0
z = -35.59

print(type(x), x)
print(type(y), y)
print(type(z), z)

#float can be scientific with an 'e', to indicate power of 10
x = 35e3
y = 12E4
z = -87.7e100

print(type(x), x)
print(type(y), y)
print(type(z), z)

#complex numbers are written with 'j'a as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x), x)
print(type(y), y)
print(type(z), z)

#convert one type to another
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print("Type:", type(a), "Value:", a)
print("Type:", type(b), "value:", b)
print("Type:", type(c), "value:", c)

#random number generation
import random

print("Random number:", random.randrange(1,10))
x = random.randrange(5, 20)

print("Type:", type(x), "Value:", x)

