from django.urls import path

from .room import RoomView

app_name = "api_v1_rooms"

urlpatterns = [
    path("", RoomView.as_view(), name="rooms"),
]
