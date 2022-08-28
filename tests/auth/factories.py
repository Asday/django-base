from django.conf import settings

import factory


class User(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")

    class Meta:
        model = settings.AUTH_USER_MODEL
