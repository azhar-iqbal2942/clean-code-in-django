from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes

from apps.handlers.room_handler import RoomHandler
from apps.serializers.room_serializer import RoomSerializer


class RoomView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="min_price",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                description="Set the Minimum price of the room you are looking for.",
            ),
            OpenApiParameter(
                name="max_price",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                description="Set the Maximum price of the room you are looking for.",
            ),
        ],
        tags=["Room"],
        operation_id="room",
        description="List all the rooms available based on the provided query params.",
        responses={200: RoomSerializer(many=True)},
    )
    def get(self, request):
        return RoomHandler().handle_get_room_list(request)
