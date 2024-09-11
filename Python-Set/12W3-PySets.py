# set - unordered unchangeable unindexed
# does not allow duplicate

myset = {"apple", "banana", "cherry"}
print(myset)

myset = {"apple", "banana", "cherry", "apple"}
print(myset)

#True and 1 are considered same value in set
#False and 0 are considered same value in set
myset = {"apple", "banana", "cherry", 1, True}
print(myset)

myset = {"apple", "banana", "cherry", 1, True, False, 0}
print(myset)

print(len(myset))

myset = {"abc", 34, True, 40, "male"}
print(myset)
print(type(myset))

#set constructor

thisset = set(("apple", "banana", "cherry"))
print(thisset)