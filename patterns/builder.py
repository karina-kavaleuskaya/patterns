from abc import ABC, abstractmethod
from enum import Enum


class Car:
    def __init__(self):
        self.components = []

    def add_component(self, component: str):
        self.components.append(component)

    def about_car(self) -> str:
        return "Car components:\n" + "\n".join(self.components)


# Enum для типов двигателей
class EngineType(Enum):
    SPORT = "sport"
    REGULAR = "regular"
    TRUCK = "truck"


# Enum для типов корпусов
class BodyType(Enum):
    SPORT = "sport"
    REGULAR = "regular"
    TRUCK = "truck"


# Абстрактные классы для компонентов
class Engine(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Body(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


# Конкретные классы для двигателей
class SportEngine(Engine):
    def get_description(self) -> str:
        return "Sport Engine"


class RegularEngine(Engine):
    def get_description(self) -> str:
        return "Regular Engine"


class TruckEngine(Engine):
    def get_description(self) -> str:
        return "Truck Engine"


# Конкретные классы для корпусов
class SportBody(Body):
    def get_description(self) -> str:
        return "Sport Body"


class RegularBody(Body):
    def get_description(self) -> str:
        return "Regular Body"


class TruckBody(Body):
    def get_description(self) -> str:
        return "Truck Body"


# Заводы для компонентов
class EngineFactory(ABC):
    @abstractmethod
    def create_engine(self, engine_type: EngineType) -> Engine:
        pass


class BodyFactory(ABC):
    @abstractmethod
    def create_body(self, body_type: BodyType) -> Body:
        pass


# Конкретные заводы для двигателей
class ConcreteEngineFactory(EngineFactory):
    def create_engine(self, engine_type: EngineType) -> Engine:
        if engine_type == EngineType.SPORT:
            return SportEngine()
        elif engine_type == EngineType.REGULAR:
            return RegularEngine()
        elif engine_type == EngineType.TRUCK:
            return TruckEngine()
        else:
            raise ValueError("Unknown engine type")


# Конкретные заводы для корпусов
class ConcreteBodyFactory(BodyFactory):
    def create_body(self, body_type: BodyType) -> Body:
        if body_type == BodyType.SPORT:
            return SportBody()
        elif body_type == BodyType.REGULAR:
            return RegularBody()
        elif body_type == BodyType.TRUCK:
            return TruckBody()
        else:
            raise ValueError("Unknown body type")


# Строитель
class CarBuilder:
    def __init__(self, engine_factory: EngineFactory, body_factory: BodyFactory):
        self.engine_factory = engine_factory
        self.body_factory = body_factory
        self.car = Car()

    def build_car(self, engine_type: EngineType, body_type: BodyType):
        engine = self.engine_factory.create_engine(engine_type)
        body = self.body_factory.create_body(body_type)
        self.car.add_component(engine.get_description())
        self.car.add_component(body.get_description())

    def get_car(self) -> Car:
        return self.car


if __name__ == "__main__":
    # Создание заводов
    engine_factory = ConcreteEngineFactory()
    body_factory = ConcreteBodyFactory()

    # Создание спортивного автомобиля
    sport_car_builder = CarBuilder(engine_factory, body_factory)
    sport_car_builder.build_car(engine_type=EngineType.SPORT, body_type=BodyType.SPORT)
    sport_car = sport_car_builder.get_car()
    print("Sport Car:\n", sport_car.about_car())

    print('*' * 40)

    # Создание обычного автомобиля
    regular_car_builder = CarBuilder(engine_factory, body_factory)
    regular_car_builder.build_car(engine_type=EngineType.REGULAR, body_type=BodyType.REGULAR)
    regular_car = regular_car_builder.get_car()
    print("Regular Car:\n", regular_car.about_car())

    print('*' * 40)

    # Создание грузовика
    truck_car_builder = CarBuilder(engine_factory, body_factory)
    truck_car_builder.build_car(engine_type=EngineType.TRUCK, body_type=BodyType.TRUCK)
    truck_car = truck_car_builder.get_car()
    print("Truck Car:\n", truck_car.about_car())

