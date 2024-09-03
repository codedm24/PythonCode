age = 36
# string and int concatenation error
# txt = "My name is John, I am " + age
txt = "My name is John, I am"
print(txt, age)

txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 *59} dollars"
print(txt)