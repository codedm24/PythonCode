thisset = { "apple", "banana", "cherry" }
thisset.add("orange")
print(thisset)

# add sets
thisset = { "apple", "banana", "cherry" }
anotherset = {"pineapple", "mango", "papaya"}
thisset.update(anotherset)
print(thisset)

thisset = { "apple", "banana", "cherry" }
thislist = ["kiwi", "orange"]
thisset.update(thislist)
print(thisset)