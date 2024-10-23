from abc import ABCMeta, abstractmethod


class Engine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass


class SportCarEngine(Engine):
    def release_engine(self):
        print( 'Engine for sport car')


class TruckEngine(Engine):
    def release_engine(self):
        print('Engine for truck')


class Car(metaclass=ABCMeta):
    @abstractmethod
    def start(self, engine:Engine):
        pass


class SportCar(Car):
    def start(self, engine:Engine):
        engine.release_engine()
        return 'Sport car is ready'


class TruckCar(Car):
    def start(self, engine:Engine):
        engine.release_engine()
        return 'Truck is ready'


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_car(self):
        pass


class SportCarFactory(Factory):
    def create_engine(self) -> Engine:
        return SportCarEngine()

    def create_car(self) -> Car:
        return SportCar()


class TruckFactory(Factory):
    def create_engine(self) -> Engine:
        return TruckEngine()

    def create_car(self) -> Car:
        return TruckCar()


if __name__ == "__main__":

    sportcar_factory = SportCarFactory()
    sportcar_engine = sportcar_factory.create_engine()
    sportcar = sportcar_factory.create_car()

    print(sportcar.start(sportcar_engine))

    truck_factory = TruckFactory()
    truck_engine = truck_factory.create_engine()
    truck = truck_factory.create_car()

    print(truck.start(truck_engine))