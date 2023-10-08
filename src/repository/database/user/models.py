from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.mixins import CreatedAndUpdatedAtMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, CreatedAndUpdatedAtMixin):
    """Custom User models that use email instead of username for login"""

    first_name = models.CharField(verbose_name="first name", max_length=20)
    last_name = models.CharField(verbose_name="last name", max_length=20)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    is_active = models.BooleanField(
        default=False, help_text="Used to activate user through email"
    )
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def full_name(self):
        """Return customer's full name"""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["id"]
