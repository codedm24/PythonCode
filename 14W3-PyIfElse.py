#if else
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif b > a:
    print("b is less than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a and b are equal")

print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are true")

if a > b or a > c:
    print("At least one of the conditions is true")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")        
else:
    print("a is greater than b")    

a = 33
b = 200

if b > a:
    pass

x = 41
if x  > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")    