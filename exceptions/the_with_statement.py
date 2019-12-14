"""
If an object has __enter__() and __exit__() magic methods, they support the
'context management protocol' allowing us to use the with statement
"""

from pathlib import Path

path = Path(__file__)
parent = path.parent
txt_file = parent/"file.txt"
exists = Path.exists(txt_file)

#  open one resource
with open( parent/"file.txt") as file:
    print(file.readlines())

#  open multiple resources at once
with open(parent/"file.txt") as file, open(parent/"another.txt") as another:
    print(file.readlines())
    print(another.readlines())

