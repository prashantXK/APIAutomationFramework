#create booking
#updated booking
#auth token

#CREATE BOOKING-----

import os
from dotenv import load_dotenv

def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

#UPDATE BOOKING-----

def payload_update_booking():
    payload = {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    return payload


#CREATE TOKEN-----

def create_token_payload():
    load_dotenv()
    username = os.getenv("USERNAME", "").strip()
    password = os.getenv("PASSWORD", "").strip()

    print(f"Final Username: {username}")  # Debugging
    print(f"Final Password: {password}")  # Debugging

    payload = {"username": username, "password": password}
    print("Payload Sent to API:", payload)  # Debugging

    return payload