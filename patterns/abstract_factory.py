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
        return f"Regular Car with {self.engine.get_type()} and {self.wheel.get_type()} ."


# Абстрактные фабрики для компонентов
class EngineFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass


class WheelFactory(ABC):
    @abstractmethod
    def create_wheel(self) -> Wheel:
        pass


# Конкретные фабрики для двигателей
class SportsEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return V8Engine()


class RegularEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return V6Engine()


# Конкретные фабрики для колес
class SportsWheelFactory(WheelFactory):
    def create_wheel(self) -> Wheel:
        return SportsWheel()


class RegularWheelFactory(WheelFactory):
    def create_wheel(self) -> Wheel:
        return RegularWheel()


# Фабрика автомобилей, использующая фабрики компонентов
class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass


class SportsCarFactory(CarFactory):
    def create_car(self) -> Car:
        engine_factory = SportsEngineFactory()
        wheel_factory = SportsWheelFactory()
        return SportsCar(engine_factory.create_engine(), wheel_factory.create_wheel())


class RegularCarFactory(CarFactory):
    def create_car(self) -> Car:
        engine_factory = RegularEngineFactory()
        wheel_factory = RegularWheelFactory()
        return RegularCar(engine_factory.create_engine(), wheel_factory.create_wheel())


if __name__ == "__main__":
    sports_factory = SportsCarFactory()
    sports_car = sports_factory.create_car()
    print(sports_car.get_description())

    print('*' * 40)

    regular_factory = RegularCarFactory()
    regular_car = regular_factory.create_car()
    print(regular_car.get_description())