#create booking
#updated booking
#auth token

#CREATE BOOKING-----

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

def payload_create_token():
    payload = {
    "username" : "admin",
    "password" : "password123"
}
    return payload