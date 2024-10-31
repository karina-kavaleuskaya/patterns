from abc import ABC, abstractmethod



class TypedList:
    def __init__(self):
        self._items = []

    def add(self, item) -> None:
        self._items.append(item)

    def get_items(self):
        return self._items


# Абстрактные классы для автомобилей и их частей
class Engine:
    def __init__(self, cylinders, displacement):
        self.cylinders = cylinders
        self.displacement = displacement

    def get_type(self):
        return f"{self.__class__.__name__} with {self.cylinders} cylinders and {self.displacement}L displacement."


class Wheel(ABC):
    @abstractmethod
    def get_type(self):
        pass


class Car:
    def __init__(self, engine, wheel):
        self.engine = engine
        self.wheel = wheel

    def get_description(self):
        return f"{self.__class__.__name__} with {self.engine.get_type()} and {self.wheel.get_type()}."


# Конкретные классы для двигателей
class V8Engine(Engine):
    pass


class V6Engine(Engine):
    pass


# Конкретные классы для колес
class SportsWheel(Wheel):
    def get_type(self):
        return "sport weels"


class RegularWheel(Wheel):
    def get_type(self):
        return "regular wheels"


# Конкретные классы для автомобилей
class SportsCar(Car):
    pass


class RegularCar(Car):
    pass

# Абстрактные фабрики для компонентов
class EngineFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass


class WheelFactory(ABC):
    @abstractmethod
    def create_wheel(self) -> Wheel:
        pass


# Конкретные фабрики для двигателей
class SportsEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return V8Engine(cylinders=8, displacement=2.5)


class RegularEngineFactory(EngineFactory):
    def create_engine(self) -> Engine:
        return V6Engine(cylinders=6, displacement=1.8)


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
    engine_list = TypedList()
    engine_list.add(V8Engine(cylinders=8, displacement=2.5))
    engine_list.add((V6Engine(cylinders=6, displacement=1.8)))

    print('Engines in List:')
    for engine in engine_list.get_items():
        print(engine.get_type())

    sports_factory = SportsCarFactory()
    sports_car = sports_factory.create_car()
    print(sports_car.get_description())

    print('*' * 40)

    regular_factory = RegularCarFactory()
    regular_car = regular_factory.create_car()
    print(regular_car.get_description())