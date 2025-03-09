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