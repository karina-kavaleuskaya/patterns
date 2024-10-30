import abc
from typing import List


class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit(self, place: 'Factory'):
        pass


class Factory(metaclass=abc.ABCMeta):
    def accept(self, visitor: Visitor):
        pass


class EngineFactory(Factory):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class CarFactory(Factory):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class TruckFactory(Factory):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class SportCarFactory(Factory):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Trip(Visitor):
    def __init__(self):
        self.value = ''

    def visit(self, place: Factory):
        if isinstance(place, CarFactory):
            self.value = 'Car on car factory is great'

        elif isinstance(place, EngineFactory):
            self.value = 'Engine could be different'

        elif isinstance(place, TruckFactory):
            self.value = 'Truck is so big'

        elif isinstance(place, SportCarFactory):
            self.value = 'Spotr car is expensive'


if __name__ == '__main__':
    places: List[Factory] = [EngineFactory(),
                             CarFactory(),
                            TruckFactory(),
                            SportCarFactory()]

    for place in places:
        visitor = Trip()
        place.accept(visitor)
        print(visitor.value)
