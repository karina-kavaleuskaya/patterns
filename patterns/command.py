import abc
from typing import List, Deque


class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def positive(self):
        pass

    @abc.abstractmethod
    def negative(self):
        pass


class Car:
    def on(self):
        print('Car is started')

    def off(self):
        print('Car is stopped')

    def speed_increase(self):
        print('Car ride faster')

    def speed_decrease(self):
        print('Car ride slowly')


class CarEngineCommand(ICommand):
    def __init__(self, car: Car):
        self.car: Car = car

    def positive(self):
        self.car.on()

    def negative(self):
        self.car.off()


class CarSpeedSystem(ICommand):
    def __init__(self, car: Car):
        self.car: Car = car

    def positive(self):
        self.car.speed_increase()

    def negative(self):
        self.car.speed_decrease()


class Multipult:
    def __init__(self):
        self.__commands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__commands[button] = command

    def init_car(self, button: int):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def stop_car(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


if __name__ == '__main__':
    car = Car()

    multipult = Multipult()
    multipult.set_command(0, CarEngineCommand(car))
    multipult.set_command(1, CarSpeedSystem(car))

    multipult.init_car(0)
    multipult.init_car(1)
    multipult.stop_car()
    multipult.stop_car()