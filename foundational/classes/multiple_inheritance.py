class Flyer:
    """
    An object that knows how to fly
    """

    def fly(self):
        print('fly')


class Swimmer:
    """
    An object that knows how to swim
    """

    def swim(self):
        print('swim')


class FlyingFish(Swimmer, Flyer):
    pass


ff = FlyingFish()
ff.fly()
ff.swim()
