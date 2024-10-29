class Car:
    _instance = None

    def __init__(self):
        self.engine = 'V8'
        self.transmission = 'Automatic'


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Car, cls).__new__(cls)
        return cls._instance


    def start(self):
        return "Car is ready to go!"

    def get_specs(self):
        return f"Engine: {self.engine}, Transmission: {self.transmission}"


if __name__ == "__main__":
    car1 = Car()
    car2 = car1

    print(car1.start())
    print(car1.get_specs())

    if car1 is car2:
        print("car1 и car2 - это один и тот же экземпляр.")
    else:
        print("car1 и car2 - разные экземпляры.")