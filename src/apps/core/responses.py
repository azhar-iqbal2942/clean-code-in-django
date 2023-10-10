from rest_framework import status
from rest_framework.response import Response as BaseResponse


class Response(BaseResponse):
    def __init__(
        self, data=None, status_code=status.HTTP_200_OK, message=None, success=True
    ):
        response_data = {
            "success": success,
            "status_code": status_code,
            "message": message,
            "data": data,
        }
        super().__init__(data=response_data, status=status_code)
