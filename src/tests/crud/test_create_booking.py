import pytest
import allure
import requests
import logging  #use to print the messages or logs

from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payloads import payload_create_booking
from src.helpers.verification import *  #import all the verification
from src.utils.utils import Utils


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking id shouldn't be null")
    @allure.description("Creating a Booking from the payload and verify that booking is should not be null")

    def test_create_booking_positive_tc1(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase of TestCreateBooking")
        LOGGER.info("POST Req Started")
        response = post_request(
            url = APIConstants().url_create_booking(),
            auth = None,
            headers = Utils().common_headers_json(),
            payload = payload_create_booking(),
            in_json = False
        )
        LOGGER.info("POST Req Done")
        LOGGER.info("Now Verify")
        verify_http_status_code(response_data=response, expected_data=
                                200)
        LOGGER.info(response.json())
        LOGGER.info(response.json()["bookingid"])
        verify_json_key_not_none(response.json()["bookingid"])
        verify_json_key_should_be_greater_than_zero(response.json()["bookingid"])

    @pytest.mark.negative
    @allure.title("Verify response of  create booking with invalid payload")
    @allure.description("Creating a Booking with the empty payload")
    def test_create_booking_negative_tc2(self):
        response = post_request(
            url = APIConstants().url_create_booking(),
            auth = None,
            headers = Utils().common_headers_json(),
            payload = {},
            in_json = False

        )
        verify_http_status_code(response_data=response, expected_data= 500)


    @pytest.mark.negative
    @allure.title("Verify response of  create booking with invalid payload 2")
    @allure.description("Creating a Booking with the invalid payload")
    def test_create_booking_negative_tc3(self):
        response = post_request(
            url = APIConstants().url_create_booking(),
            auth = None,
            headers = Utils().common_headers_json(),
            payload = {},
            in_json = False

        )
        verify_http_status_code(response_data=response, expected_data= 500)






























