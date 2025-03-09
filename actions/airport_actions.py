from typing import Text, Dict, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionGetName(Action):
    def name(self) -> Text:
        return "action_get_airports"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='')
        return []