
class Location:
    def __init__(self, city: str, state: str, country: str, zipcode: str):
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def get_city(self) -> str:
        return self.__city

    def get_state(self) -> str:
        return self.__state

    def get_country(self) -> str:
        return self.__country

    def get_zipcode(self) -> str:
        return self.__zipcode

    def get_location_as_string(self) -> str:
        return f'{self.__city}, {self.__state} {self.__zipcode}, {self.__country}'