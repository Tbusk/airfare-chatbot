from datetime import datetime
from typing import List

from airfare.aircraft import Aircraft
from airfare.location import Location
from airfare.flight import Flight

aircraft_no_one = Aircraft(1, 120)
aircraft_no_two = Aircraft(2, 120)
aircraft_no_three = Aircraft(3, 120)
aircraft_no_four = Aircraft(4, 120)
aircraft_no_five = Aircraft(5, 120)

detroit_to_petoskey = Flight(1, Location('Detroit', 'Michigan', 'United States', '48021'),
                             Location('Petoskey', 'Michigan', 'United States', '49770'), datetime(2025, 3, 10, 5),
                             datetime(2025, 3, 10, 6), aircraft_no_one, 320.00)
detroit_to_lansing = Flight(2, Location('Detroit', 'Michigan', 'United States', '48021'),
                            Location('Lansing', 'Michigan', 'United States', '48901'), datetime(2025, 3, 10, 6),
                            datetime(2025, 3, 10, 7), aircraft_no_two, 345.00)
detroit_to_kalamazoo = Flight(3, Location('Detroit', 'Michigan', 'United States', '48021'),
                              Location('Kalamazoo', 'Michigan', 'United States', '49001'), datetime(2025, 3, 10, 7),
                              datetime(2025, 3, 10, 8), aircraft_no_three, 425.00)
detroit_to_big_rapids = Flight(4, Location('Detroit', 'Michigan', 'United States', '48021'),
                               Location('Big Rapids', 'Michigan', 'United States', '49307'), datetime(2025, 3, 10, 8),
                               datetime(2025, 3, 10, 10), aircraft_no_four, 225.00)
detroit_to_iron_mountain = Flight(5, Location('Detroit', 'Michigan', 'United States', '48021'),
                                  Location('Iron Mountain', 'Michigan', 'United States', '49801'),
                                  datetime(2025, 3, 10, 9), datetime(2025, 3, 10, 12), aircraft_no_five, 325.00)

scheduled_flights: List[Flight] = [detroit_to_petoskey, detroit_to_lansing, detroit_to_kalamazoo, detroit_to_big_rapids,
                                   detroit_to_iron_mountain]


def book_flight(flight: Flight):
    scheduled_flights.append(flight)


def cancel_flight(flight_number: int):
    for flight in scheduled_flights:
        if flight.get_flight_number() == flight_number:
            scheduled_flights.remove(flight)
            return
