from abc import ABC, abstractmethod
from enum import Enum


class GreetingType(Enum):
    MORNING = 'Good morning!'
    DAY = 'Good day!'
    NIGHT = 'Good night!'


class Greeter(ABC):
    def __init__(self, greeting: GreetingType):
        self.greeting = greeting

    @abstractmethod
    def greet(self, name: str) -> str:
        pass


class MorningGreeter(Greeter):
    def __init__(self):
        super().__init__(GreetingType.MORNING)

    def greet(self, name: str) -> str:
        return f"{self.greeting.value} {name}"


class DayGreeter(Greeter):
    def __init__(self):
        super().__init__(GreetingType.DAY)

    def greet(self, name: str) -> str:
        return f"{self.greeting.value} {name}"


class NightGreeter(Greeter):
    def __init__(self):
        super().__init__(GreetingType.NIGHT)

    def greet(self, name: str) -> str:
        return f"{self.greeting.value} {name}"


def greet(name: str, greeting: GreetingType) -> str:
    greeting_classes = {
        GreetingType.MORNING: MorningGreeter,
        GreetingType.DAY: DayGreeter,
        GreetingType.NIGHT: NightGreeter,
    }

    greeter_class = greeting_classes.get(greeting)

    greeter = greeter_class()
    return greeter.greet(name)




if __name__ == "__main__":
    name = "Vova"

    print(greet(name, GreetingType.MORNING))
    print(greet(name, GreetingType.DAY))
    print(greet(name, GreetingType.NIGHT))
