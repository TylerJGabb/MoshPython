"""
If an object has __enter__() and __exit__() magic methods, they support the
'context management protocol' allowing us to use the with statement
"""

#  open one resource
with open("file.txt") as file:
    print(file.readlines())

#  open multiple resources at once
with open("file.txt") as file, open("another.txt") as another:
    print(file.readlines())
    print(another.readlines())

