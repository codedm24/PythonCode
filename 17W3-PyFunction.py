#function
print("function 1")
def my_function():
    print("Hello from a function")

my_function()

print("function 2")

def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")

print("function 3")

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Tobias","Refsnes")

print("function 4")

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil","Tobias","Linus")   

print("function 5")

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("function 6")

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("function 7")

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("India")
my_function()

print("Loop 8")

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

print("function 9")

def my_function(x):
    return 5 * x

print(my_function(3))

print("function 10")

def my_function():
    pass

print("function 11")

def my_function(x, /):
    print(x)

my_function(3)
# error my_function(x = 3)

print("function 12")

def my_function(*, x):
    print(x)

my_function(x=3)
#error my_function(3)

print("function 13")

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

print("function 14")

def tri_recusrion(k):
    if k > 0:
        result = k + tri_recusrion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recusrion(6)
