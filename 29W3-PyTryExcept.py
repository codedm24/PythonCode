#try except
print("Try Except 1")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occured")
finally:
    print("The 'try except' is finished")

print("Try Except 2")
try:
    print("Hello")
except:
    print("Somethin went wrong")
else:
    print("Nothing went wrong")  

print("Try except 3")
x = -1
if(x < 0):
    raise Exception("Sorry no numbers below zero")

print("Try Except 4")

x= "hello"
if(not type(x) is int):
    raise TypeError("Only integers are allowed")