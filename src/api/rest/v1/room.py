from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class RoomView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(data={"data": "Working"}, status=status.HTTP_200_OK)
