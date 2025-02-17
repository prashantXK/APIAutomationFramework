# To reuse Create Token and Create Booking

# To reuse create token create booking
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.verification import *
from src.helpers.payloads import *
from src.utils.utils import Utils

from dotenv import load_dotenv
import os
import allure
import pytest
import requests

load_dotenv()  # Ensure this is called early in the script

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print(f"Loaded Username: {username}")  # Debug check

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url = APIConstants().url_create_token(),
        headers= Utils().common_headers_json(),
        auth = None,
        payload= create_token_payload(),
        in_json = False
    )
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
    response_data = response.json()
    if "token" not in response_data:
        reason = response_data.get('reason', 'Unknown error')
        raise ValueError(f"Failed to create token. Reason: {reason}")

    token = response_data["token"]
    verify_json_key_not_none(token)
    return token



@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url = APIConstants().url_create_booking(),
        auth = None,
        headers=Utils().common_headers_json(),
        payload= payload_create_booking(),
        in_json = False
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response, expected_data=200)
    verify_json_key_not_none(booking_id)
    return booking_id











































