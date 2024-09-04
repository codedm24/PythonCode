# capitalize first letter - Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
print(txt.capitalize())

txt = "python is FUN!"
print(txt.capitalize())

txt = "36 is my age"
print(txt.capitalize())

#casefold - make the string lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center - The center() method will center align the string,
#  using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(20)
print(x)
x = txt.center(20,"*")
print(x)

#count - returns the number of times a 
# specified value appears in the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

x = txt.count("apple",10,24)
print(x)

#encode - The encode() method encodes the string, 
# using the specified encoding. If no encoding is 
# specified, UTF-8 will be used.
txt = "My name is stale"
x = txt.encode()
print(x)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#endswith - returns True if the string ends with the 
# specified value, otherwise False.
txt = "Hello, welcome to my world."
x =txt.endswith('.')
print(x)
x = txt.endswith(txt,5,11)
print(x)

#expandtabs - sets the tab size to the
#specified number of whitespaces
#default tab size is 8
txt = "H\te\tl\tl\to"
x = txt.expandtabs()
print(x)
x = txt.expandtabs(2)
print(x)
x = txt.expandtabs(4)
print(x)
x = txt.expandtabs(10)
print(x)

#find - finds the first occurrence of the specified value.
txt = "Hello, welcome to my world."
x = txt.find('welcome')
print(x)
x = txt.find('e')
print(x)

#format - format the specified value and insert
#them inside the string's placeholder
txt = "My name is {fname}, I'm {age}".format(fname="John",age=36)
print(txt)
txt = "My name is {0}, I'm {1}".format("John",36)
print(txt)
txt = "My name is {}, I'm {}".format("John",36)
print(txt)
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
#Use "-" to always indicate if the number is negative 
# (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
#Use " " (a space) to insert a space before positive numbers 
# and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
#Use "c" to convert the number into unicode format:
txt = "The binary version of {0} is {0:c}"
print(txt.format(5))
#Use "d" to convert the number into decimal format:
txt = "The binary version of {0} is {0:d}"
print(txt.format(0b101))
#Use "e" to convert a number into scientific 
# number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5))
#Use "f" to convert a number into a fixed point number, 
# default with 6 decimals, but use a period followed by 
# a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))
#without the ".2" inside the placeholder, 
# this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))
#Use "F" to convert a number into a fixed point number, 
# but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))
#general format
txt = "The price is {:g} dollars."
print(txt.format(45))
#general format upper case E for scientific notation
txt = "The price is {:E} dollars."
print(txt.format(45))
#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
#number format
txt = "The number format version of {0} is {0:n}"
print(txt.format(255))
#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))

#index -  method finds the first occurrence of the specified value.
txt = "Hello, welcome to my world!"
x = txt.index("welcome")
print(x)
x = txt.index("e",5,10)
print(x)

#isalnum - Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha - Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isascii - Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal - Returns True if all characters in the string are decimals
txt  = "1234"
x = txt.isdecimal()
print(x)
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

#isdigit - Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)

#isidentifier - Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x)
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#islower - Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

#isnumeric - 	Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)

#isprintable - Returns True if all characters in the string are printable
