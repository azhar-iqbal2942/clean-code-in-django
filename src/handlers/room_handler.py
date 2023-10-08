from django.http import HttpRequest

from services.room_service import RoomFilter
from repository.database.room.models import Room


class RoomHandler:
    def handle_get_room_list(self, request: HttpRequest):
        params = request.query_params  # type: ignore
        qs = Room.objects.all()

        filtered = RoomFilter(params, qs)
        print(filtered.qs)
        return None
