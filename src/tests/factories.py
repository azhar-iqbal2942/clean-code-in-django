# type: ignore
import factory
from apps.repository.database.models import User, Room


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    code = factory.Faker("uuid4")
    size = factory.Faker("random_int", min=10, max=1000)
    price = factory.Faker("random_element", elements=(19.99, 2.99, 5.99, 10.99))
    longitude = factory.Faker(
        "random_element", elements=(-0.09998975, 0.18228006, 0.27891577, 0.33894476)
    )
    latitude = factory.Faker(
        "random_element", elements=(51.75436293, 51.74640997, 51.45994069, 51.39916678)
    )


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: f"john{n}")
    last_name = factory.Sequence(lambda n: f"doe{n}")
    email = factory.Sequence(lambda n: f"lennon{n}@thebeatles.com")
    password = factory.PostGenerationMethodCall("set_password", "secure_password")
