from abc import ABC, abstractmethod
from enum import StrEnum
import os
import importlib.util
import random
import time
from typing import Dict, Union

alpha = 'abcdefghijklmnopqrstuvwxyz'


class GreetingType(StrEnum):
    MORNING = 'morning!'
    DAY = 'day!'
    NIGHT = 'night!'
    HELLO = 'hello'
    HI = 'hi'


class Greeter(ABC):

    @abstractmethod
    def greet(self, name: str) -> str:
        pass

    def name(self):
        return str(self.__class__)


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
        self._name = greeting

    def greet(self, name: str) -> str:
        return f"{self.greeting} {name}"

    def name(self):
        return self._name


def load_greeter_config(config_path: str) -> str:
    spec = importlib.util.spec_from_file_location("configs", config_path)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)
    return config_module.greeting



def initialize_custom_greeters(config_dir: str) -> dict:
    greeters = {}
    for filename in os.listdir(config_dir):
        if filename.endswith('.py'):
            greeting = load_greeter_config(os.path.join(config_dir, filename))
            greeter_name = filename.split('.')[0]
            greeters[greeter_name] = CustomGreetingGreeter(greeting)
    return greeters


greeting_classes: Dict[Union[GreetingType, str], Greeter] = {
    GreetingType.MORNING: MorningGreeter(),
    GreetingType.DAY: DayGreeter(),
    GreetingType.NIGHT: NightGreeter(),
}

custom_greeting_classes = initialize_custom_greeters('configs')
greeting_classes.update(custom_greeting_classes)

def greet(name: str, greeting: Union[GreetingType, str]) -> str:
    greeter = greeting_classes.get(greeting)

    if greeter is None:
        raise ValueError("Invalid greeter type provided.")
    return greeter.greet(name)


def greet_two(name: str, greeting: GreetingType or str) -> str:
    greeting_class = {
        GreetingType.MORNING: MorningGreeter(),
        GreetingType.DAY: DayGreeter(),
        GreetingType.NIGHT: NightGreeter(),
    }

    custom_greeting_class = initialize_custom_greeters('configs')
    greeting_class.update(custom_greeting_class)

    greeter = greeting_class.get(greeting)

    if greeter is None:
        raise ValueError("Invalid greeter type provided.")

    return greeter.greet(name)


if __name__ == "__main__":
    start_time = time.time()
    with open('people.txt', 'r') as f:
        for line in f:
            gtype = random.choice(alpha) + random.choice(alpha)
            gtype_2 = random.choice(alpha) + random.choice(alpha)
            print(greet(line, gtype), greet(line, gtype_2))

    end_time = time.time()
    duration = end_time - start_time

    start_time_2 = time.time()
    with open('people.txt', 'r') as f:
        for line in f:
            gtype = random.choice(alpha) + random.choice(alpha)
            gtype_2 = random.choice(alpha) + random.choice(alpha)
            print(greet_two(line, gtype), greet_two(line, gtype_2))

    end_time_2 = time.time()
    duration_2 = end_time_2 - start_time_2


    print(f"Code executed in {duration:.4f} seconds")
    print(f"Code executed in {duration_2:.4f} seconds, dict")

    #for greeting_type in GreetingType:
    #    print(greet(name, greeting_type))