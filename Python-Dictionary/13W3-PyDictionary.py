#dictionary
#ordered changeable do not allow duplicates

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)
print(thisdict["brand"])

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}

print(thisdict)
print(len(thisdict))

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "colors" : ["red", "white", "blue" ]
}

print(thisdict)
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

