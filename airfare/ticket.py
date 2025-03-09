class Ticket:

    def __init__(self, ticket_id, from_airport, to_airport, price, departure_time, expected_duration_minutes):
        self.ticket_id = ticket_id
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.departure_time = departure_time
        self.expected_duration_minutes = expected_duration_minutes
        self.price = price

    def get_from_airport(self):
        return self.from_airport

    def get_to_airport(self):
        return self.to_airport

    def get_departure_time(self):
        return self.departure_time

    def get_expected_duration_minutes(self):
        return self.expected_duration_minutes

    def get_price(self):
        return self.price