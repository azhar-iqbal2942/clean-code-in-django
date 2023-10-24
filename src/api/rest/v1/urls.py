from django.urls import path, include


urlpatterns = [
    path("rooms/", include("api.rest.v1.room.urls", namespace="v1_rooms")),
]
