#python scope

print("Scope 1")

def myfunction():
    x = 300
    print(x)

myfunction()

print("Scope 2")

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

print("scope 3")

x = 400

def myfunc():
    print(x)
    # error as it is treated as local variable x = 500

myfunc()

print(x)

print("scope 4")

def myfunc():
    global x
    print(x)
    x = 500
myfunc()
print(x)

print("scope 5")

def myfunc():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc())