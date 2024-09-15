#set methods

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.add("apple")
print(fruits)

fruits.clear()
print(fruits)

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

z = x - y
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
myset = x.difference(y,z)
print(myset)
myset = x - y - z
print(myset)

x.difference_update(y)
print(x)

x -= y
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

fruits = {"apple", "banana", "cherry"}
company = {"google", "microsoft", "apple"}
set3 = fruits.intersection(company)
print(set3)
set3 = fruits & company
print(set3)

x = {'a','b','c'}
y = {'c','d','e'}
z = {'f','g','c'}
result = x.intersection(y,z)
print(result)

result = x & y & z
print(result)

x.intersection_update(y)
print(x)
print(y)

x.intersection_update(y,z)
print(x)

x &= y
print(x)

x = {'a','b','c'}
y = {'c','d','e'}
z = {'f','g','c'}

x &= y & z
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

y = {"google", "microsoft", "Apple"}
z = x.isdisjoint(y)
print(z)


y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

x = {"a","b","c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print("subest: ",z)

z = x <= y
print(z)

y = {"f", "e", "d", "b", "a"}
z = x.issubset(y)
print(z)

y = {"a","b","c"}
x = {"f", "e", "d", "c", "b", "a"}
z = x.issuperset(y)
print("superset: ",z)
z = x >= y
print(z)

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)


fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

z = x ^ y
print(z)

x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

z = x | y
print(z)

x = {'a','b','c'}
y = {'f', 'd', 'a'}
z = {'c', 'd', 'e'}
result = x.union(y,z)
print(result)

result = x | y | z
print(result)     

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print("update: ",x)

x |= y
print("update with symbol: ",x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x |= y | z
print(x)