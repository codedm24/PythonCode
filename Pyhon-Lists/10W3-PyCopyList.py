thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple","banana","cherry"]
#mylist = list(["apple","banana","cherry"])
mylist = list(thislist)
print(mylist)

thislist = ["apple","banana","cherry"]
mylist = thislist[:]
print(mylist)
print("reverse list")
mylist = thislist[::-1]
print(mylist)

thislist = ["apple","banana","cherry"]
mylist = thislist[0:2]
print(mylist)