from typing import List

from airfare.airport import Airport


class Airline:

    def __init__(self, airline_id: int, name: str, airports: List[Airport]):
        self.airline_id = airline_id
        self.name = name
        self.airports = airports

    def add_airport(self, airport: Airport):
        self.airports.append(airport)

    def get_airports(self) -> List[Airport]:
        return self.airports

    def get_airline_id(self) -> int:
        return self.airline_id

    def get_name(self) -> str:
        return self.name