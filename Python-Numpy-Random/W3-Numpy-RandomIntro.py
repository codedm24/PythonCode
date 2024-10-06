# numpy random intro
from numpy import random

print('generate random int number')
x = random.randint(100)
print(x)

print('generate random float number')
x = random.rand()
print(x)

print('Generate 1-D array int')
arr = random.randint(100,size=5)
print(arr)

print('Generate 2-D array int')
arr = random.randint(100, size=(3,5))
print(arr)

print('Generate 1-D array float')
arr = random.rand(5)
print(arr)
print(type(arr))

print('Generate 2-D array float')
arr = random.rand(3,5)
print(arr)
print(arr.dtype)

print('Random number of choice')
x = random.choice([3,5,7,9])
print(x)
x = random.choice([3,5,7,9])
print(x)

print('Generate 2-D array using number of choice')
x = random.choice([3,5,7,9],size=(3,5))
print(x)