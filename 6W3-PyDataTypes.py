#string data type
'''print the type as str'''
x= "Hello World!"
xType = type(x)
print(type(x))
print(x)
print("Type:", type(x), "Value:", x)
print("Type: " + str(xType) + " Value: " + str(x))
#setting specific data type
x = str("Hello")
print(type(x), x)
print("")

#integer data type
'''print the type as int'''
x = 5
print(type(x))
print(x)
#setting specific data type
x = int(5)
print(type(x), x)
print()

#float data type
'''print the type as float'''
x = 20.5
print(type(x))
print(x)
#setting specific data type
x = float(20.5)
print(type(x), x)
print()

#complex data type
'''print the type as complex'''
x = 1j
print(type(x))
print(x)
#setting specific data type
x = complex(1j)
print(type(x), x)
print()

#list data type
'''print the type as list'''
x = ["apple", "banana", "cherry"]
print(type(x))
print(x)
#setting specific data type
x = list(("apple","banana","cherry"))
print(type(x), x)
print()

#tuple data type
'''print the type as tuple'''
x = ("apple", "banana", "cherry")
print(type(x))
print(x)
#setting specific data type
x = tuple(("apple","banana","cherry"))
print(type(x), x)
print()

#range data type
'''print the type as range'''
x = range(6)
print(type(x))
print(x)
print()

#Dictionary data type
'''print the type as dict'''
x = {"name": "John", "age" : 36}
print(type(x))
print(x)
#setting specific data type
x = dict(name="John",age=36)
print(type(x), x)
print()

#Set data type
'''print the type as set'''
x = {"apple", "banana", "cherry"}
print(type(x))
print(x)
#setting specific data type
x = set(("apple", "banana", "cherry"))
print(type(x), x)
print()

#Frozenset data type
'''print the type as frozenset'''
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
print(x)
print()

#Boolean data type
'''print the type as bool'''
x = True
print(type(x))
print(x)
#setting specific data type
x = bool(5)
print(type(x), x)
x = bool(0)
print(type(x), x)
print()

#Byte data type
'''print the type as bytes'''
x = b"Hello"
print(type(x))
print(x)
x= bytes(5)
print(type(x), x)
x= bytes('Hello',"UTF-8")
print(type(x), x)
print()

#ByteArray data type
'''print the type as bytearray'''
x = bytearray(5)
print(type(x))
print(x)
x = bytearray("Hello World!","UTF-8")
print(type(x), x)
print()

#MemoryView data type
'''print the type as memoryview'''
x = memoryview(bytes(5))
print(type(x))
print(x)
x = memoryview(bytearray("Hello World!","UTF-8"))
print(type(x), x)
print()

#None data type
'''print the type as nontype'''
x = None
print(type(x))
print(x)
if (x == None): # check None value
    print(f"x is {type(x)}")