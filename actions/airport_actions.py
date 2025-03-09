from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from airfare import airline

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text='I\'m sorry. I\'m afraid I don\'t know how to respond to that. Please ask me something else.')
        return []

class ActionGetNumberOfFlights(Action):

    def name(self) -> Text:
        return "action_get_number_of_scheduled_flights"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flights = airline.scheduled_flights

        dispatcher.utter_message(text=f'There are {len(flights)} flights scheduled.')
        return []

class ActionGetListOfFlights(Action):

    def name(self) -> Text:
        return "action_get_list_of_scheduled_flights"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flights = airline.scheduled_flights

        flight_list = ''

        for index, flight in enumerate(flights):
            flight_list += f'{index + 1}. Flight #{flight.get_flight_number()} - {flight.get_departure_time()} departure and {flight.get_estimated_arrival_time()} arrival from {flight.get_departure_location().get_location_as_string()} to {flight.get_arrival_location().get_location_as_string()}.\n'

        dispatcher.utter_message(text=f'This is the active schedule:\n\n {flight_list}')
        return []

class ActionGetArrivalLocation(Action):
    def name(self) -> Text:
        return "action_get_arrival_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        flights = airline.scheduled_flights

        flight_number = tracker.get_slot('flight_number')

        for flight in flights:
            if flight.get_flight_number() == int(flight_number):
                dispatcher.utter_message(text=f'{flight.get_arrival_location().get_location_as_string()}.')
                return []

        dispatcher.utter_message(text=f'Couldn\'t find a flight with number {flight_number}.  Please check that you entered it correctly and try again.')

        return []

class ActionGetDepartureLocation(Action):
    def name(self) -> Text:
        return "action_get_departure_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        flights = airline.scheduled_flights

        flight_number = tracker.get_slot('flight_number')

        for flight in flights:
            if flight.get_flight_number() == int(flight_number):
                dispatcher.utter_message(text=f'{flight.get_departure_location().get_location_as_string()}.')
                return []

        dispatcher.utter_message(text=f'Couldn\'t find a flight with number {flight_number}.  Please check that you entered it correctly and try again.')

        return []

class ActionGetDepartureDateAndTime(Action):
    def name(self) -> Text:
        return "action_get_departure_date_and_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flights = airline.scheduled_flights

        flight_number = tracker.get_slot('flight_number')

        for flight in flights:
            if flight.get_flight_number() == int(flight_number):

                departure_datetime = flight.get_departure_time()
                departure_date = departure_datetime.date().strftime('%B %d, %Y')
                departure_time = departure_datetime.strftime('%I:%M %p')


                dispatcher.utter_message(text=f'{departure_date} at {departure_time}.')
                return []

        dispatcher.utter_message(text=f'Couldn\'t find a flight with number {flight_number}.  Please check that you entered it correctly and try again.')

        return []

class ActionGetFlightPrice(Action):

    def name(self) -> Text:
        return "action_get_flight_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flights = airline.scheduled_flights

        flight_number = tracker.get_slot('flight_number')

        for flight in flights:
            if flight.get_flight_number() == int(flight_number):
                price = flight.get_price()
                dispatcher.utter_message(text=f'That flight costs ${price}.')
                return []

        dispatcher.utter_message(text=f'Couldn\'t find a flight with number {flight_number}.  Please check that you entered it correctly and try again.')
        return []