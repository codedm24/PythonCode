thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict.pop("model")

print(thisdict)

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict.popitem()
print(thisdict)

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del thisdict["year"]
print(thisdict)

thisdict.clear()
print(thisdict)