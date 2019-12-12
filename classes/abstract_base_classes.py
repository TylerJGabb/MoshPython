from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open!')
        self.opened = True
        print('stream opened')

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed!')
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('reading data from a file')


class NetworkStream(Stream):
    def read(self):
        print('reading data from a network')


class MemoryStream(Stream):
    pass


fs = FileStream()
ns = NetworkStream()
ms = MemoryStream()  # this will raise TypeError because abstract methods not initialized
