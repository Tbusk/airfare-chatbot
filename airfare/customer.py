from typing import List

from airfare.flight import Flight


class Customer:
    def __init__(self, first_name: str, last_name: str, date_of_birth: str, flights: List[Flight]):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__flights = flights

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_date_of_birth(self) -> str:
        return self.__date_of_birth

    def get_flights(self) -> List[Flight]:
        return self.__flights

    def book_flight(self, flight: Flight):
        self.__flights.append(flight)

    def cancel_flight(self, flight_number: int):
        for flight in self.__flights:
            if flight.get_flight_number() == flight_number:
                self.__flights.remove(flight)
                return