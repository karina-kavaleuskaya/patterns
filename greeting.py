from enum import Enum


class GreetingType(Enum):
    MORNING = 'Good morning!'
    DAY = 'Good day!'
    NIGHT = 'Good night!'


def greet(name: str, greeting: GreetingType):
    greetings = {
        GreetingType.MORNING: f"{GreetingType.MORNING.value} {name}",
        GreetingType.DAY: f"{GreetingType.DAY.value} {name}",
        GreetingType.NIGHT: f"{GreetingType.NIGHT.value} {name}"
    }
    return greetings.get(greeting)


if __name__ == "__main__":
    name = "Vova"

    print(greet(name, GreetingType.MORNING))
    print(greet(name, GreetingType.DAY))
    print(greet(name, GreetingType.NIGHT))