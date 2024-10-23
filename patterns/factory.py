class Engine:
    def __init__(self):
        pass


class Transmission:
    def __init__(self):
        pass


class Gears:
    def __init__(self):
        pass


class BrakeSystem:
    def __init__(self):
        pass


class SteeringSystem:
    def __init__(self):
        pass


class Car:
    def __init__(self, engine: Engine, transmission: Transmission,
                 gears: Gears, brake_system:BrakeSystem , steering_system: SteeringSystem):
        self.engine = engine
        self.transmission = transmission
        self.gears = gears
        self.brake_system = brake_system
        self.steering_system = steering_system

    def start(self):
        return "Car is ready"


class Truck(Car):
    def start(self):
        return "Truck is ready"


class Factory():
    def create(self):
        pass


class CarFactory(Factory):
    def create(self):
        engine = Engine()
        transmission = Transmission()
        gears = Gears()
        brake_system = BrakeSystem()
        steering_system = SteeringSystem()
        return Car(engine, transmission, gears, brake_system, steering_system)


class TruckFactory(Factory):
    def create(self):
        engine = Engine()
        transmission = Transmission()
        gears = Gears()
        brake_system = BrakeSystem()
        steering_system = SteeringSystem()
        return Truck(engine, transmission, gears, brake_system, steering_system)


if __name__ == "__main__":

    factory = CarFactory()
    car = factory.create()

    factory = TruckFactory()
    truck = factory.create()


    print(car.start())
    print(truck.start())
