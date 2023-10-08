from django.urls import path

from .room import RoomView

urlpatterns = [
    path("rooms", RoomView.as_view()),
]
