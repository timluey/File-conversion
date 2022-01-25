#pip install attr

import attr

@attr.s(auto_attribs=True)
class Im:
    hi : int

file = open(r"File conversion project\case3.sw", "r")

lines=file.readlines()

print (lines[1])
print(type(lines[1]))
