thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict["model"])

x = thisdict.get("model")
print(x)

keys = thisdict.keys()
print(keys)

values = thisdict.values()
print(values)

thisdict["color"] = "white"
print(thisdict)

thisdict["year"] = 2020
print(thisdict)

thisdict["color"] = "red"
print(thisdict)

print(thisdict.items())

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")