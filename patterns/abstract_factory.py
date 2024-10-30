from abc import ABC, abstractmethod


# Абстрактные классы для автомобилей и их частей
class Engine(ABC):
    @abstractmethod
    def get_type(self):
        pass


class Wheel(ABC):
    @abstractmethod
    def get_type(self):
        pass

class Car(ABC):
    @abstractmethod
    def get_description(self):
        pass


# Конкретные классы для двигателей
class V8Engine(Engine):
    def get_type(self):
        return "V8 Engine"


class V6Engine(Engine):
    def get_type(self):
        return "V6 Engine"


# Конкретные классы для колес
class SportsWheel(Wheel):
    def get_type(self):
        return "sport weels"


class RegularWheel(Wheel):
    def get_type(self):
        return "regular wheels"


# Конкретные классы для автомобилей
class SportsCar(Car):
    def __init__(self, engine: Engine, wheel: Wheel):
        self.engine = engine
        self.wheel = wheel

    def get_description(self):
        return f"Sports Car with {self.engine.get_type()} and {self.wheel.get_type()}."


class RegularCar(Car):
    def __init__(self, engine: Engine, wheel: Wheel):
        self.engine = engine
        self.wheel = wheel

    def get_description(self):
        return f"Regular Car with {self.engine.get_type()} and {self.wheel.get_type()} wheels."


# Абстрактные фабрики для двигателя
class EngineFactory(ABC):
    @abstractmethod
    def create_v6_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_v8_engine(self) -> Engine:
        pass


# Абстрактные фабрики для колес
class WheelFactory(ABC):
    @abstractmethod
    def create_sports_wheel(self) -> Wheel:
        pass

    @abstractmethod
    def create_regular_wheel(self) -> Wheel:
        pass


# Конкретные фабрики для двигателей
class ConcreteEngineFactory(EngineFactory):
    def create_v6_engine(self) -> Engine:
        return V6Engine()

    def create_v8_engine(self) -> Engine:
        return V8Engine()


# Конкретные фабрики для колес
class ConcreteWheelFactory(WheelFactory):
    def create_sports_wheel(self) -> Wheel:
        return SportsWheel()

    def create_regular_wheel(self) -> Wheel:
        return RegularWheel()


# Фабрики автомобилей
class CarFactory(ABC):
    @abstractmethod
    def create_car(self, engine_factory: EngineFactory, wheel_factory: WheelFactory) -> Car:
        pass


class SportsCarFactory(CarFactory):
    def create_car(self, engine_factory: EngineFactory, wheel_factory: WheelFactory) -> Car:
        engine = engine_factory.create_v8_engine()
        wheel = wheel_factory.create_sports_wheel()
        return SportsCar(engine, wheel)


class RegularCarFactory(CarFactory):
    def create_car(self, engine_factory: EngineFactory, wheel_factory: WheelFactory) -> Car:
        engine = engine_factory.create_v6_engine()
        wheel = wheel_factory.create_regular_wheel()
        return RegularCar(engine, wheel)


if __name__ == "__main__":

    engine_factory = ConcreteEngineFactory()
    wheel_factory = ConcreteWheelFactory()


    sports_factory = SportsCarFactory()
    sports_car = sports_factory.create_car(engine_factory, wheel_factory)
    print(sports_car.get_description())


    regular_factory = RegularCarFactory()
    regular_car = regular_factory.create_car(engine_factory, wheel_factory)
    print(regular_car.get_description())