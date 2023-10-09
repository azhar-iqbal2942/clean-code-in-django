from django.db import models


class CreatedAndUpdatedAtMixin(models.Model):
    """
    This mixin introduces two new fields that store the created at and updated at
    timestamps.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
