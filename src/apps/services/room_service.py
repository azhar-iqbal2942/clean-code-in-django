from django_filters import rest_framework as filters

from apps.repository.database.models import Room


class RoomService:
    def get_room_list(self):
        pass


class RoomFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gt")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Room
        fields = ["price"]
