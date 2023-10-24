from django.urls import path

from .room import RoomView

app_name = "v1_rooms"

urlpatterns = [
    path("", RoomView.as_view(), name="rooms"),
]
