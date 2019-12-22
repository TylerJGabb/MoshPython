class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price can not be negative')
        self.__price = value


p = Product(10)
print(p.price)
p.price = -1
