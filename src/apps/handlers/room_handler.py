from django.http import HttpRequest
from rest_framework import status

from apps.services.room_service import RoomFilter
from apps.repository.database.models import Room
from apps.serializers.room_serializer import RoomSerializer
from apps.core.responses import Response


class RoomHandler:
    def handle_get_room_list(self, request: HttpRequest):
        params = request.query_params  # type: ignore
        queryset = Room.objects.all()
        try:
            filtered_data = RoomFilter(params, queryset)
            serializer = RoomSerializer(filtered_data.qs, many=True)  # type: ignore
            return Response(data=serializer.data)
        except Exception as exc:
            return Response(
                message=str(exc),
                status_code=status.HTTP_400_BAD_REQUEST,
                success=False,
            )
