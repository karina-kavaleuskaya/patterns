# Базовый класс для машины
class Car:
    def __init__(self):
        self.description = "Car"
        self.power = 150

    def get_description(self):
        return self.description

    def get_power(self):
        return self.power


class NitroSystem:
    def __init__(self, car):
        self.car = car

    def get_description(self):
        return self.car.get_description() + " with nitro system"

    def get_power(self):
        return self.car.get_power() + 50


if __name__ == "__main__":

    car = Car()
    print(car.get_description())
    print("Power:", car.get_power())

    print('-' * 30)

    sport_car = NitroSystem(car)
    print(sport_car.get_description())
    print("Power:", sport_car.get_power())