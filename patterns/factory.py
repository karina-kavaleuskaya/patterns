class Engine:
    def __init__(self, type_name="Ordinary"):
        self.type_name = type_name


class EngineFactory:
    def create_engine(self):
        return Engine()


class SportsEngineFactory(EngineFactory):
    def create_engine(self):
        print('Creating a sports car engine')
        return Engine(type_name="Sports")


class TruckEngineFactory(EngineFactory):
    def create_engine(self):
        print('Creating a truck engine')
        return Engine(type_name="Truck")


class Transmission:
    def __init__(self):
        pass


class Gears:
    def __init__(self):
        pass


class BrakeSystem:
    def __init__(self):
        pass


class Shell:
    def __init__(self, type_name="Ordinary"):
        self.type_name = type_name


class ShellFactory:
    def create_shell(self):
        return Shell()


class SportsShellFactory(ShellFactory):
    def create_shell(self):
        print('Creating a sports shell')
        return Shell(type_name="Sports")


class Car:
    def __init__(self, engine: Engine, transmission: Transmission,
                 gears: Gears, brake_system: BrakeSystem, shell: Shell):
        self.engine = engine
        self.transmission = transmission
        self.gears = gears
        self.brake_system = brake_system
        self.shell = shell

    def start(self):
        return "Car is ready"

    def __str__(self):
        return (f"Car: {self.engine.type_name} engine, "
                f"{self.shell.type_name} shell.")


class Truck(Car):
    def start(self):
        return "Truck is ready"

    def __str__(self):
        return (f"Truck: {self.engine.type_name} engine, "
                f"{self.shell.type_name} shell.")


class Factory:
    def create(self):
        pass


class CarFactory(Factory):
    def __init__(self, engine_factory: EngineFactory, shell_factory: ShellFactory):
        self.engine_factory = engine_factory
        self.shell_factory = shell_factory

    def create(self):
        engine = self.engine_factory.create_engine()
        transmission = Transmission()
        gears = Gears()
        brake_system = BrakeSystem()
        shell = self.shell_factory.create_shell()
        return Car(engine, transmission, gears, brake_system, shell)


class TruckFactory(Factory):
    def create(self):
        engine = TruckEngineFactory().create_engine()
        transmission = Transmission()
        gears = Gears()
        brake_system = BrakeSystem()
        shell = Shell()
        return Truck(engine, transmission, gears, brake_system, shell)


# Example usage
if __name__ == "__main__":

    racing_car_factory = CarFactory(SportsEngineFactory(), SportsShellFactory())
    sports_car = racing_car_factory.create()
    print(sports_car.start())
    print(sports_car)

    # Create a regular car
    car_factory = CarFactory(EngineFactory(), ShellFactory())
    car = car_factory.create()
    print(car.start())
    print(car)

    # Create a truck
    truck_factory = TruckFactory()
    truck = truck_factory.create()
    print(truck.start())
    print(truck)