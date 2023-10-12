import pytest


@pytest.mark.django_db
def test_user_user_factory(user_factory):
    user = user_factory()
    assert user.first_name == "john0"
    assert user.email == "lennon0@thebeatles.com"
    assert user.check_password("secure_password")
