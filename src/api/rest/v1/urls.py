from django.urls import path, include


urlpatterns = [
    path("rooms/", include("api.rest.v1.room.urls", namespace="api_v1_rooms")),
]
