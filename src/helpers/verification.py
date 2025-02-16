#ASSERTIONS----

def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code == expected_data, "Failed to get the status"


def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to match the key"


def verify_json_key_not_null(key):
    assert key != 0, "Failed! key is null"


def verify_json_key_should_be_greater_than_zero(key):
    assert key > 0, "Failed! key !> 0"

