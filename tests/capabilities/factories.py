from random import choice

import factory
from faker.providers import BaseProvider

from ..auth.factories import User


class Capability(factory.django.DjangoModelFactory):
    name = factory.Faker("capability_name")

    class Meta:
        model = "capabilities.Capability"


class Can(factory.django.DjangoModelFactory):
    user = factory.SubFactory(User)
    capability = factory.SubFactory(Capability)

    class Meta:
        model = "capabilities.Can"


class Implication(factory.django.DjangoModelFactory):
    capability = factory.SubFactory(Capability)
    implies = factory.SubFactory(Capability)

    class Meta:
        model = "capabilities.Implication"


class CapabilitiesProvider(BaseProvider):

    def capability_name(self):
        return choice([
            "add users",
            "view users",
            "change users",
            "delete users",
            "administer deployments",
            "rollback changes",
            "contact users",
            "run marketing campaigns",
            "view historic trends",
            "start expensive jobs",
            "change billing information",
            "revoke licenses",
            "restart the server",
        ])
