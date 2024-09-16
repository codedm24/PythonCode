#while loop
print("Loop 1")
i = 1
while i < 6:
    print(i)
    i += 1

print("Loop 2")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("Loop 3")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue;
    print(i)        

print("Loop 4")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")        