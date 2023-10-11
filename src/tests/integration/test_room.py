import pytest
from django.urls import reverse

pytestmark = pytest.mark.integration


@pytest.mark.django_db
def test_room_with_no_query_param(api_client):
    url = reverse("rooms")
    http_response = api_client.get(url)

    assert http_response.status_code == 200
