from abc import ABC, abstractmethod
from enum import Enum
import os
import importlib.util


class GreetingType(Enum):
    MORNING = 'morning!'
    DAY = 'day!'
    NIGHT = 'night!'
    HELLO = 'hello'
    HI = 'hi'


class Greeter(ABC):

    @abstractmethod
    def greet(self, name: str) -> str:
        pass


class MorningGreeter(Greeter):

    def greet(self, name: str) -> str:
        return f"Good morning! {name}"


class DayGreeter(Greeter):

    def greet(self, name: str) -> str:
        return f"Good day! {name}"


class NightGreeter(Greeter):
    def greet(self, name: str) -> str:
        return f"Good morning! {name}"


class CustomGreetingGreeter(Greeter):
    def __init__(self, greeting: str):
        self.greeting = greeting

    def greet(self, name: str) -> str:
        return f"{self.greeting} {name}"


def load_greeter_config(config_path: str) -> str:
    spec = importlib.util.spec_from_file_location("configs", config_path)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)
    return config_module.greeting



def initialize_custom_greeters(config_dir: str) -> dict:
    greeters = {}
    for filename in os.listdir(config_dir):
        if filename.endswith('_config.py'):
            greeting = load_greeter_config(os.path.join(config_dir, filename))
            greeter_name = filename.split('_')[0].upper()
            greeters[GreetingType[greeter_name]] = CustomGreetingGreeter(greeting)
    return greeters


def greet(name: str, greeting: GreetingType) -> str:
    greeting_classes = {
        GreetingType.MORNING: MorningGreeter(),
        GreetingType.DAY: DayGreeter(),
        GreetingType.NIGHT: NightGreeter(),
    }

    custom_greeting_classes = initialize_custom_greeters('configs')
    greeting_classes.update(custom_greeting_classes)

    greeter = greeting_classes.get(greeting)

    if greeter is None:
        raise ValueError("Invalid greeter type provided.")

    return greeter.greet(name)


if __name__ == "__main__":
    name = "Dasha"

    for greeting_type in GreetingType:
        print(greet(name, greeting_type))