fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]
fruits.extend(cars)
print(fruits)

fruits = ["apple", "banana", "cherry"]
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

fruits = ["apple", "banana", "cherry"]
#gives error
#x = fruits.index("orange")
#print(x)
if "orange" in fruits:
    x = fruits.index("orange")
    print(x)
else:
    print("Orange not there in fruits")
x = fruits.index("banana")
print(x)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)
#index out of range error
#fruits.pop(4)
#print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

cars = ["Ford", "BMW", "Volvo"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

def MyFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key= MyFunc)
print(cars)

def MyFunc(e):
    return e['year']

cars = [
    {'car' :'Ford','year' : 2005},
    {'car' :'Mitsubishi', 'year' : 2000},
    {'car' : 'BMW', 'year' : 2019},
    {'car' : 'VW', 'year' : 2011}
]
cars.sort(key= MyFunc)
print(cars)

def MyFunc(e):
    return len(e)
cars = ['Ford','Mitsubishi','BMW','VW']
cars.sort(reverse=True, key=MyFunc)
print(cars)



