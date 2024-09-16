#For loop
print("Loop 1")
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

print("Loop 2")
for x in "banana":
    print(x)

print("Loop 3")
for x in fruits:
    print(x)
    if x == "banana":
        break

print("Loop 4")
for x in fruits:
    print(x)
    if x == "banana":
        continue

print("Loop 5")    
for x in range(6):
    print(x)

print("Loop 6")
for x in range(2,6):
    print(x)

print("Loop 7")
for x in range(2,10,3):
    print(x)

print("Loop 8")
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("Loop 9")    
adj = ["red","big","tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
        
print("Loop 10")
for x in [0, 1, 2]:
    pass
                    