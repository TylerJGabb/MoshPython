from collections import namedtuple

"""
sometimes we don't really need a class if all we are doing is storing data, so in this case
we can use the data class "named tuple" that allows us to create objects in a way that is 
expliciy and everything is name

In this case, checking equality will only validate that data fields are equal, and does not care
about the memory address of each object
"""
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(f'addr of p1 = {id(p1)}')
print(f'addr of p2 = {id(p2)}')
print(f'p1 == p2 -> {p1 == p2}')
