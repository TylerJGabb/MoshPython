class TagCloud:
    def __init__(self):
        #  prefixing with double underscore __ makes this field private, and so that it can't be accessed publicly
        #  its doesn't actually prevent it, just makes it difficult to access it
        self.__tags = {}

    def add(self, tag):
        #  get the current count for tag, if there is none, initialize it to zero, and then increment by one
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    #  adds support for cloud[key]
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    #  adds support for cloud[key] = value
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    #  adds support for len(cloud)
    def __len__(self):
        return len(self.__tags)

    #  adds support for iterating over this cloud
    def __iter__(self):
        return iter(self.__tags)


def demo():
    cloud = TagCloud()
    cloud.add('tyler')
    cloud.add('mosh')
    cloud.add('Doodoo')
    cloud.add('doodoo')
    print(f"cloud['not_exist']={cloud['not_exist']}")


def demo_private_field():
    cloud = TagCloud()
    print(cloud.__tags)
