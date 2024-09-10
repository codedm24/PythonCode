thistuple = ("apple","banana","cherry")
print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi","melon","mango")
print(thistuple[2:5]) #print from index 2(included) to index 5(not included)
print(thistuple[:4]) #print 0-3 item or 4 items from first
print(thistuple[2:]) #print items from first to last except first two items
print(thistuple[-4:-1]) #print 4-1 or 3 items from second last items

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")