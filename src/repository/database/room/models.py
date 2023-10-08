from django.db import models

from core.mixins import CreatedAndUpdatedAtMixin
from core.utils import float_to_integer


class Room(CreatedAndUpdatedAtMixin, models.Model):
    code = models.CharField(max_length=36, null=False)
    size = models.IntegerField()
    price = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self) -> str:
        return f"Size: {self.size} -- price:{self.price}"

    def save(self, *args, **kwargs):
        self.price = float_to_integer(self.price)
        super(Room, self).save(*args, **kwargs)
