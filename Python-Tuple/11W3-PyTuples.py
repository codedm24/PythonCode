mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))
print(type(mytuple))

#one item tuple
mytuple = ("apple",)
print(type(mytuple))

#not tuple
mytuple = ("apple")
print(type(mytuple))

#can be of different type
tuple1 = ("apple","banana","cherry")
tuple2 = (1,5,7,9)
tuple3 = (True, False, True)
tuple4 = ("abc",34, True,40,"male")

thistuple = tuple(("Apple","Banana","Cherry"))
print(thistuple)
print(type(thistuple))