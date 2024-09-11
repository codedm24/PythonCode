# join sets
#union join both items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2,set3, set4)
print(myset)

myset = set1 | set2 | set3 | set4
print(myset)

set1 = {"a","b","c"}
tuple1 = (1,2,3)
myset = set1.union(tuple1)
print(myset)
# raises error
#myset = set1 | tuple1
#print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#intersection keeps only the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"microsoft", "google", "apple"}
set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#difference return a new set that will contain items from first set only
#that are not present in second set
set1 = {"apple","banana","cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)

set1 = {"apple","banana","cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# will keep items from both sets that are not duplicates
set1 = {"apple","banana","cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2
print(set3)

set1.symmetric_difference_update(set2)
print(set1)