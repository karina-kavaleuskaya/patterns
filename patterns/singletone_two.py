class SingletonA:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonA, cls).__new__(cls)
        return cls._instance

    def start(self):
        return "Singleton A is ready"


class SingletonB(SingletonA):
    def start(self):
        return "Singleton B is ready"


if __name__ == "__main__":
    instance_a1 = SingletonA()
    print(instance_a1.start())

    instance_b1 = SingletonB()
    print(instance_b1.start())

    print(f"instance_a1 is instance_b1: {instance_a1 is instance_b1}")