myFamily = {
    "child1" : {
        "name":"Emil",
        "year":2004
    },
    "child2" :{
        "name":"Tobias",
        "year":2007
    },
    "child3": {
        "name":"Linus",
        "year":2011
    }
}

print(myFamily)

child1 = {
        "name":"Emil",
        "year":2004
    }
child2 = {
        "name":"Tobias",
        "year":2007
    }
child3 = {
        "name":"Linus",
        "year":2011
    }

myFamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myFamily["child2"]["name"])

for x,obj in myFamily.items():
    print(x)
    print("Sub dictionary")
    for y in obj:
        print(y + ':', obj[y])