#json

import json 

print("json loads - convert to object")
x = '{"name":"John","age":30,"city":"New York"}'
y = json.loads(x)
print(y)
print(y["age"])

print("json dumps - conver to json")
x = {
    "name": "John",
    "age":36,
    "city":"New York"
}
y = json.dumps(x)
print(y)
print(json.dumps({"name":"John","age":36}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
#error cannot convert set
# print(json.dumps({"apple", "banana", "cherry"}))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(None))

x = {
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children": ["Ann", "Billy"],
    "pets":None,
    "cars":[
        {"model" : "BMW 230","mpg":27.5},
        {"model" : "Ford Edge", "mpg":24.1}
    ]
}

print(json.dumps(x))
print(json.dumps(x,indent=4,separators=(". ", " = "),sort_keys=True))