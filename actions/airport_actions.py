from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import airfare.airfare_application as app
from airfare.airline import Airline


class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_airlines"

    def format_list(self, airlines: List[Airline]):
        if len(airlines) == 1:
            return airlines[0]
        return ', '.join(airline.name for airline in airlines[:-1]) + ', and ' + airlines[-1].name

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f'A few of them are {self.format_list(app.Airlines[:5])}.' )
        return []