from abc import ABCMeta, abstractmethod


class Engine(metaclass=ABCMeta):
    @abstractmethod
    def description(self):
        pass


class SportCarEngine(Engine):
    def description(self):
        print('Engine for sport car')


class TruckEngine(Engine):
    def description(self):
        print('Engine for truck')


class Car(metaclass=ABCMeta):
    @abstractmethod
    def initialize(self, engine: Engine):
        pass


class SportCar(Car):
    def initialize(self, engine: Engine):
        engine.description()
        return 'Sport car is ready'


class TruckCar(Car):
    def initialize(self, engine: Engine):
        engine.description()
        return 'Truck is ready'


class EngineFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass


class SportCarEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return SportCarEngine()


class TruckEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return TruckEngine()


class CarFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_car(self) -> Car:
        pass


class SportCarFactory(CarFactory):
    def create_car(self) -> Car:
        return SportCar()


class TruckFactory(CarFactory):
    def create_car(self) -> Car:
        return TruckCar()



if __name__ == "__main__":

    sport_factory = SportCarFactory()
    sport_engine_factory = SportCarEngineFactory()
    sport_car = sport_factory.create_car()
    sport_engine = sport_engine_factory.create_engine()
    print(sport_car.initialize(sport_engine))  # Engine for sport car; Sport car is ready


    truck_factory = TruckFactory()
    truck_engine_factory = TruckEngineFactory()
    truck_car = truck_factory.create_car()
    truck_engine = truck_engine_factory.create_engine()
    print(truck_car.initialize(truck_engine))  # Engine for truck; Truck is ready