#module

import importlib
module_name = '24W3-PyModule'
mymodule = importlib.import_module(module_name)
import platform

mymodule.greeting("Mike")

a = mymodule.person1["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform)
print(x)
print(platform.win32_edition)
