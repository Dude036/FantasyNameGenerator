from abc import abstractmethod, ABCMeta


class Character(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate():
        pass

    def __str__(self):
        return self.generate()

    def __repr__(self):
        return self.generate()

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate()


class Store(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate():
        pass

    def __str__(self):
        return self.generate()

    def __repr__(self):
        return self.generate()

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate()


class Item(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate():
        pass

    def __str__(self):
        return self.generate()

    def __repr__(self):
        return self.generate()

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate()
