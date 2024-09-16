#file read
import datetime
import os

print("File read 1")
f = open("links.txt")
print(f.read())
#f.close()

print("File read 2")
f = open("links.txt","r")
print(f.read(5))
f.close()

print("file read 3")
f = open("links.txt","r")
print(f.readline())
print(f.readline())
f.close()

print("file read 4")
f = open("links.txt","r")
i = 0
for x in f:
    i += 1
    print(x)
    if i == 5:
        break

print("file write 1")
f = open("links.txt","a")
f.write("Now the file has more content!")
f.close()
f = open("links.txt","r")
print(f.read())
f.close()

print("file write 2")
f = open("newlinks.txt","w")
f.write("Woops! I have deleted the content")
f.close()
f = open("newlinks.txt","r")
print(f.read())
f.close()

print("file write 3")
f = open("newlinks1.txt","x")
f.write("New file created: {0} ".format(datetime.datetime.now()))
f.close()

print("file write 4")
f = open("newlinks1.txt","a")
f.write("New file created: {0}".format(datetime.datetime.now().strftime("%x")))
f.close()
f = open("newlinks1.txt","r")
print(f.readlines())
f.close()

print("file delete 1")
os.remove("newlinks1.txt")
if(not os.path.exists("newlinks1.txt")):
    print("file deleted")

print("file delete 2")
if(os.path.exists("newlinks1.txt")):
    os.remove("newlinks1.txt")
    print("file deleted")
else:
    print("The file does not exist")