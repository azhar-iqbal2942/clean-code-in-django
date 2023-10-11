# type: ignore
import factory

from django.contrib.auth.models import Group
from apps.repository.database.user.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: f"john{n}")
    last_name = factory.Sequence(lambda n: f"doe{n}")
    email = factory.Sequence(lambda n: f"lennon{n}@thebeatles.com")
    password = factory.PostGenerationMethodCall("set_password", "secure_password")


@factory.post_generation
def has_default_group(self, create, extracted, **kwargs):
    if not create:
        return
    if extracted:
        default_group, _ = Group.objects.get_or_create(name="group")
        self.groups.add(default_group)
