from airfare.airplane import Airplane


class Airport:

    def __init__(self, airport_id: int, city: str, state: str, country: str, zipcode: str):
        self.airport_id = airport_id
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
        self.airplanes = []

    def add_airplane(self, airplane: Airplane):
        self.airplanes.append(airplane)

    def remove_airplane(self, airplane: Airplane):
        self.airplanes.remove(airplane)

    def get_airport_id(self):
        return self.airport_id

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_zipcode(self):
        return self.zipcode

    def get_airplanes(self):
        return self.airplanes