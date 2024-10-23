from abc import ABCMeta


class Car:
    def __init__(self):
        self.data: str = ''

    def about_car(self) -> str:
        return  self.data

    def append_data(self, string: str):
        self.data += string


class Factory(metaclass=ABCMeta):
    def crete_engine(self):
        pass

    def create_transmission(self):
        pass

    def create_gears(self):
        pass

    def create_brake_sys(self):
        pass

    def get_car(self) -> Car:
        pass


class SportCarFactory(Factory):

    def __init__(self):
        self.__car = Car()

    def crete_engine(self):
        self.__car.append_data('Engine for sport car is ready')

    def create_transmission(self):
        self.__car.append_data('Transmission for sport car is ready')

    def create_gears(self):
        self.__car.append_data('Gears for sport car is ready')

    def create_brake_sys(self):
        self.__car.append_data('Brake system for sport car is ready')

    def get_car(self) -> Car:
        return self.__car


class TruckCarFactory(Factory):

    def __init__(self):
        self.__car = Car()

    def crete_engine(self):
        self.__car.append_data('Engine for truck is ready\n',)

    def create_transmission(self):
        self.__car.append_data('Transmission for truck is ready\n')

    def create_gears(self):
        self.__car.append_data('Gears for truck is ready\n')

    def create_brake_sys(self):
        self.__car.append_data('Brake system for truck is ready\n')

    def get_car(self) -> Car:
        return self.__car


class Director:
    def __init__(self, factory: Factory):
        self.__factory = factory

    def set_factory(self, factory: Factory):
        self.__factory = factory

    def create_without_engine(self) -> Car:
        self.__factory.create_transmission()
        self.__factory.create_gears()
        self.__factory.create_brake_sys()
        return self.__factory.get_car()

    def create_ready_car(self) -> Car:
        self.__factory.crete_engine()
        self.__factory.create_transmission()
        self.__factory.create_gears()
        self.__factory.create_brake_sys()
        return self.__factory.get_car()


if __name__ == "__main__":
    sportcar_factory: Factory = SportCarFactory()

    director = Director(sportcar_factory)

    sportcar: Car = director.create_ready_car()
    print(sportcar.about_car())

    truck_factory: Factory = TruckCarFactory()
    director.set_factory(truck_factory)

    truck:  Car = director.create_without_engine()
    print(truck.about_car())
