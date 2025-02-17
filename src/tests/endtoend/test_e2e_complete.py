import allure
import pytest
import requests

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import put_request, delete_request
from src.helpers.payloads import payload_create_booking, payload_update_booking
from src.helpers.verification import verify_response_key, verify_http_status_code, verify_delete_response
from src.utils.utils import Utils


class TestE2E1:

    @allure.title("E2E - Create Booking -> Update -> Delete")
    @allure.description("Verify that created booking id when we update we able to update it and after updating we able to delete it")

    #UPDATE BOOKING-----

    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        token = create_token
        booking_id = get_booking_id
        put_url = APIConstants.url_patch_put_delete(booking_id = booking_id)
        print(put_url)
        response = put_request(
            url = put_url,
            headers=Utils.common_header_put_delete_patch_cookie(token=token),
            payload= payload_update_booking(),
            auth = None,
            in_json=False
        )

        #verifictaion
        verify_http_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json())["firstname"]
        verify_response_key(response.json())["lastname"]




    @allure.title("E2E - Delete Booking")
    @allure.description("Verify booking gets deleted with the booking id and token.")

    def test_delete_booking_id(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        token = create_token
        booking_id = get_booking_id
        delete_url = APIConstants.url_patch_put_delete(booking_id = booking_id)
        print(delete_url)
        response = delete_request(
            url=delete_url,
            headers=Utils.common_header_put_patch_delete_basic_auth(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=201)
        verify_delete_response(response.text)
























