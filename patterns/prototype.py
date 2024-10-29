import copy


class Car:
    __type: str = ''
    __params: dict = {'Engine': 'ordinary', 'Shell': 'ordinary'}

    def __init__(self, donor: 'Car' = None):
        if donor is not None:
            self.__type = donor.get_type()
            self.__params = copy.deepcopy(donor.get_params())

    def set_type(self, type: str):
        self.__type = type

    def get_type(self) -> str:
        return self.__type

    def get_params(self) -> dict:
        return self.__params

    def set_engine(self, new_engine: str) -> dict:
        self.__params['Engine'] = new_engine

    def set_shell(self, new_shell: str) -> dict:
        self.__params['Shell'] = new_shell

    def clone(self):
        return Car(self)


if __name__ == "__main__":
    car_doner: Car = Car()
    car_doner.set_type('Car')

    car_clone: Car = car_doner.clone()

    car_clone.set_engine('sport engine')
    car_clone.set_shell('sport shell')
    car_clone.set_type('Sport car')

    print('Donor: ', car_doner.get_type(), car_clone.get_params())
    print('Clone: ', car_clone.get_type(), car_clone.get_params())