from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from airfare import airline


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

        dispatcher.utter_message(text=f'Sure thing!\n\n {flight_list}')
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
