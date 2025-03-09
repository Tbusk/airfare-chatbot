from typing import List

import airfare.airport as airport


class Airline:

    def __init__(self, airline_id: int, name: str, airports: List[airport.Airport]):
        self.airline_id = airline_id
        self.name = name
        self.airports = airports

    def add_airport(self, airport: airport.Airport):
        self.airports.append(airport)

    def get_airports(self) -> List[airport.Airport]:
        return self.airports

    def get_airline_id(self) -> int:
        return self.airline_id

    def get_name(self) -> str:
        return self.name