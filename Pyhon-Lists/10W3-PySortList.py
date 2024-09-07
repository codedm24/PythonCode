thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

thislist = [23,100,65,82,50]
thislist.sort()
print(thislist)

thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [23,100,65,82,50]
thislist.sort(reverse=True)
print(thislist)

def MyFunc(n):
    print(n," ", n-50)
#    return abs(n - 50)
    return (n-50)

thislist = [23,100,65,82,50]
thislist.sort(key= MyFunc)
print(thislist)

def MyFunc(n):
    print(n," ", n-50)
    return abs(n - 50)

thislist = [23,100,65,82,50]
thislist.sort(key= MyFunc)
print(thislist)

thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.reverse()
print(thislist)

