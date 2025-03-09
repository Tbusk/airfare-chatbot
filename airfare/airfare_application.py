from typing import List

from airfare.airline import Airline
from airfare.airport import Airport

Airlines = List[Airline]

def init_airlines(self):

    lansing_airport = Airport(1, 'Lansing','Michigan', 'United States', '48906')
    detroit_airport = Airport(2, 'Detroit', 'Michigan', 'United States', '48242')

    delta_airlines = Airline(len(Airlines) + 1, 'Delta', [lansing_airport, detroit_airport])
    Airlines.append(self, delta_airlines)
    american_airlines = Airline(len(Airlines) + 1, 'American', [lansing_airport, detroit_airport])
    Airlines.append(self, american_airlines)
    united_airlines = Airline(len(Airlines) + 1, 'United', [lansing_airport, detroit_airport])
    Airlines.append(self, united_airlines)
    southwest_airlines = Airline(len(Airlines) + 1, 'Southwest', [lansing_airport, detroit_airport])
    Airlines.append(self, southwest_airlines)
    alaska_airlines = Airline(len(Airlines) + 1, 'Alaska', [lansing_airport, detroit_airport])
    Airlines.append(self, alaska_airlines)
    air_canada = Airline(len(Airlines) + 1, 'Air Canada', [lansing_airport, detroit_airport])
    Airlines.append(self, air_canada)
    jetblue_airlines = Airline(len(Airlines) + 1, 'JetBlue', [lansing_airport, detroit_airport])
    Airlines.append(self, jetblue_airlines)

def get_airlines(self) -> List[Airline]:
    return self.Airlines
