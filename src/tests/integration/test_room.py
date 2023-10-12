import pytest
from typing import List

from apps.repository.database.models import Room

pytestmark = pytest.mark.integration


@pytest.fixture
def rooms(room_factory) -> List[Room]:
    return [room_factory() for _ in range(10)]


@pytest.mark.django_db
def test_room_with_no_query_param_return_all_rooms(api_client, rooms):
    http_response = api_client.get("/api/v1/rooms")

    assert http_response.status_code == 200
    assert len(http_response.data["data"]) == 10


@pytest.mark.django_db
def test_room_with_valid_query_params_return_filtered_rooms(api_client, rooms):
    http_response = api_client.get("/api/v1/rooms?min_price=399&max_price=1099")

    print(http_response.data["data"])
    assert http_response.status_code == 200
    assert all(
        (dict(room)["price"] > 399 and dict(room)["price"] < 1099)
        for room in http_response.data["data"]
    )


@pytest.mark.django_db
def test_room_with_invalid_query_params_names_return_all_rooms(api_client, rooms):
    http_response = api_client.get("/api/v1/rooms?new_price=399&old_price=1099")

    assert http_response.status_code == 200
    assert len(http_response.data["data"]) == 10


@pytest.mark.django_db
def test_room_with_invalid_query_params_request_return_all_rooms(api_client, rooms):
    http_response = api_client.get("/api/v1/rooms?hdhdh")

    assert http_response.status_code == 200
    assert len(http_response.data["data"]) == 10
