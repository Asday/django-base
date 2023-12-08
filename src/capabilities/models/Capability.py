from django.db import models

from .constants import CAPABILITY_NAME_LENGTH


class Capability(models.Model):
    name = models.CharField(max_length=CAPABILITY_NAME_LENGTH, unique=True)

    def __str__(self):
        return self.name
