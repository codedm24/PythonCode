thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1984
}

for x in thisdict:
    print(x)
    print(thisdict[x])

for x in thisdict.values():
    print("Value: ", x)

for x in thisdict.keys():
    print("Key:", x)   

for x, y in thisdict.items():
    print("Key: ", x, ", Value: ", y)         


