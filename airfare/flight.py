from datetime import datetime

from airfare.aircraft import Aircraft
from airfare.location import Location


class Flight:
    def __init__(self, flight_number: int, departure_location: Location, arrival_location: Location, departure_time: datetime, estimated_arrival_time: datetime, aircraft: Aircraft, price: float):
        self.__flight_number = flight_number
        self.__departure_location = departure_location
        self.__arrival_location = arrival_location
        self.__departure_time = departure_time
        self.__estimated_arrival_time = estimated_arrival_time
        self.__aircraft = aircraft
        self.__price = price

    def get_flight_number(self) -> int:
        return self.__flight_number

    def get_departure_location(self) -> Location:
        return self.__departure_location

    def get_arrival_location(self) -> Location:
        return self.__arrival_location

    def get_departure_time(self) -> datetime:
        return self.__departure_time

    def get_estimated_arrival_time(self) -> datetime:
        return self.__estimated_arrival_time

    def get_price(self) -> float:
        return self.__price