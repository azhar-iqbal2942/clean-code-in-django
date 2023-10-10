import pytest
from typing import List, Optional
from django.contrib.auth.models import Group, Permission

from apps.repository.database.user.models import User

"""
Note: You can define scope of the fixture.There are multiple types of scopes supported by pytest.
- function
- class
- module
- session

--> Default value of scope is function.
Example:
@pytest.fixture(scope='module')
"""


@pytest.fixture
def app_user_group(db) -> Group:
    group = Group.objects.create(name="app_user")
    change_user_permissions = Permission.objects.filter(
        codename__in=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permissions)
    return group


@pytest.fixture
def app_user_factory(app_user_group: Group):
    # Closure function
    def create_app_user(
        password: Optional[str] = None,
        first_name: Optional[str] = "first name",
        last_name: Optional[str] = "last name",
        email: Optional[str] = "foo@bar.com",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = True,
        groups: List[Group] = [],
    ) -> User:
        user = User.objects.create_user(  # type: ignore
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        user.groups.add(app_user_group)
        user.groups.add(*groups)
        return user

    return create_app_user


@pytest.fixture
def user_A(db, app_user_factory) -> User:
    return app_user_factory("A")


@pytest.fixture
def user_B(db, app_user_factory) -> User:
    return app_user_factory("B")


def test_should_create_user_in_app_user_group(
    user_A: User,
    app_user_group: Group,
) -> None:
    assert user_A.groups.filter(pk=app_user_group.pk).exists()


def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk
