car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}

car.clear()
print(car)

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}

x = car.copy()
print(x)

x = ("key1", "key2", "key3")
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)

x = ("key1","key2","key3")
thisdict = dict.fromkeys(x)
print(thisdict)

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = car.get("model")
print(x)

x = car.get("price",15000)
print(x)

x = car.items()
print(x)

car["year"] = 2018
print(car)

x = car.keys()
print(x)

car["color"] = "white"
print(car)

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

car.pop("model")
print(car)

print("pop item")
car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
car.popitem()
print(car)

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

x = car.setdefault("model", "Bronco")
print(x)

x = car.setdefault("color","white")
print(x)

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

car.update({"color":"white"})
print(car)

print(car.values())

car["year"] = 2018
print(car)

car.pop("brand")
print(car)