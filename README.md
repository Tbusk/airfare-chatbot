# Airfare Chatbot with RASA

This is a team project in SENG355 (Software Tools) aimed at building a chatbot with RASA.  
This project uses some objects in the airfare package to simulate some connectivity to existing services for an airline 
application.

## Getting Started

Task 1: Download spacy.

Task 2: Download the medium english model with the following command:

```shell
python -m spacy download en_core_web_md
```

Execute the following commands:
1. rasa train
2. rasa run actions
3. rasa shell

Soon, you'll be able to interact with our chatbot.

## Features

1. Get how many flights are scheduled.
2. Learn what flights are scheduled.
3. Get departure location of a flight.
4. Get arrival location of a flight.
5. Get departure time of a flight.
6. Get price of a flight.
7. Get check-in procedure.
8. Get baggage policy.
9. Get flight delay policy.
10. Get ticket change / refund policy.

### Pipeline / Fallback
Original Source: https://github.com/amin3141/zir-rasabot
