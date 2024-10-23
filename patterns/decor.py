class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        pass


class Transmission:
    def __init__(self, type):
        pass


class Gears:
    def __init__(self, type):
        pass


class BrakeSystem:
    def __init__(self, type):
        pass


class SteeringSystem:
    def __init__(self, type):
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


class CarShell:
    def __init__(self, car):
        self._car = car

    def start(self):
        return self._car.start()


class Blinker(CarShell):
    def start(self):
        return f"{self._car.start()} with blinker"







if __name__ == "__main__":
    engine = Engine(horsepower=300, type="бензиновый")
    transmission = Transmission(type="автоматическая")
    gears = Gears(type="6 передач")
    brake_system = BrakeSystem(type="дисковые")
    steering_system = SteeringSystem(type="гидравлическое")

    car = Car(engine, transmission, gears, brake_system, steering_system)
    car_with_blinker = Blinker(car)


    print(car_with_blinker.start())