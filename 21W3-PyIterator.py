#iterator
print("Iterator 1")
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

myit = iter(mytuple)
for x in range(3):
    print(x)
    print(next(myit))

myit = iter(mytuple)
for x in myit:
    print(x)
 #   print(next(myit))

print("Iterator 2")
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

myit = iter(mystr)
for x in myit:
    print(x)

print("Iterator 3")
mytuple = ("apple", "banana","cherry")
for x in mytuple:
    print(x)

print("Iterator 4")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if(self.a <= 20):
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myit = iter(myclass)

for x in myit:
    print(x)
    if(x == 10):
        break
