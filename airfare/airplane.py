from airfare.airport import Airport
from airfare.ticket import Ticket


class Airplane:

    def __init__(self, airplane_id: int, airport: Airport, passenger_capacity: int, fuel_capacity: float):
        self.airplane_id = airplane_id
        self.airport = airport
        self.passenger_capacity = passenger_capacity
        self.fuel_capacity = fuel_capacity
        self.tickets = []

    def add_ticket(self, ticket: Ticket):
        if len(self.tickets) + 1 < self.passenger_capacity:
            self.tickets.append(ticket)

    def remove_ticket(self, ticket: Ticket):
        if len(self.tickets) > 0:
            self.tickets.remove(ticket)

    def get_tickets(self):
        return self.tickets

    def get_airplane_id(self):
        return self.airplane_id

    def get_passenger_capacity(self):
        return self.passenger_capacity

    def get_fuel_capacity(self):
        return self.fuel_capacity

    def get_airport(self):
        return self.airport
