# remove set items
thisset = { "apple", "banana", "cherry" }
thisset.remove("banana")
#raise error as item does not exist
#thisset.remove("mango") 
print(thisset)

thisset = { "apple", "banana", "cherry" }
thisset.discard("banana")
# does not raise error if item does not exist
thisset.discard("mango")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.pop() #remove random item
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
#raise error
#print(thisset)