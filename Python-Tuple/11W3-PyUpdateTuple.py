# To add item to tuple
# first convert it to list
# add item
# then convert back to tuple

x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)
print(x)

y.append("orange")
x = tuple(y)
print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange", )
thistuple += y
print(thistuple)

#remove item from tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #error thistuple does not exist