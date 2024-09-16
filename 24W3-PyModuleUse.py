import importlib
module_name = '24W3-PyModule'
mymodule = importlib.import_module(module_name)

mymodule.greeting("Mike")

a = mymodule.person1["age"]
print(a)

