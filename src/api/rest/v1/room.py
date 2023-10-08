from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from handlers.room_handler import RoomHandler


class RoomView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return RoomHandler().handle_get_room_list(request)
