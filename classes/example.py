class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        #  no need to specity __lt__ if __gt__ is specified unless special logic is needed
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # this is a class method
    @classmethod
    def zero(cls):
        return cls(0, 0)  # this is like calling Point(0,0)


def constructing():
    get_from_factory = Point.zero()
    make_instance = Point(1, 1)
    print(get_from_factory)
    print(make_instance)


def magic_methods():
    p1 = Point.zero()
    p2 = Point(0, 0)
    print(f'p1 == p2 -> {p1 == p2}')
    print(f'p1 > p2  -> {p1 > p2}')


magic_methods()
