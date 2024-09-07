thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple","banana","cherry"]
for i in [0,1,2]: 
    print(thislist[i])    

i = 0
thislist = ["apple","banana","cherry"]
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    