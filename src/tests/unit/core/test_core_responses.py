# type: ignore
from rest_framework import status
from apps.core.responses import Response


def test_response_success_default():
    data = {"test": "OK"}
    resp = Response(
        data=data,
    )

    assert resp.data["data"] == data
    assert resp.status_code == 200
    assert resp.data["message"] == None
    assert resp.data["success"] == True


def test_response_success_with_change_status_code():
    resp = Response(status_code=status.HTTP_201_CREATED)

    assert resp.status_code == 201


def test_response_success_with_change_message():
    message = "test_message"
    resp = Response(message=message)

    assert resp.data["message"] == message


def test_response_fail_with_change_success_flag():
    resp = Response(success=False)

    assert resp.data["success"] == False
