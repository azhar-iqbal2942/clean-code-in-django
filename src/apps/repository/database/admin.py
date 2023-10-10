from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # type: ignore

from .models import Room, User


class UserAdmin(UserAdmin):
    ordering = ("email",)
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "first_name", "last_name")

    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
        ),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "first_name", "last_name")}),
        ("Security", {"fields": ("password1", "password2")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Room)
