from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, OuterRef, Subquery

from tools import foreign_model

from .constants import CAPABILITY_NAME_LENGTH


class QuerySet(models.QuerySet):

    def denormalise_strs(self):
        User = get_user_model()
        Capability = apps.get_model("capabilities.Capability")
        (
            self
            .select_related("user", "capability")
            .annotate(
                user_username=Subquery(
                    User.objects
                    .filter(pk=OuterRef("user_id"))
                    .values("username")
                    [:1],
                ),
                capability_name=Subquery(
                    Capability.objects
                    .filter(pk=OuterRef("capability_id"))
                    .values("name")
                    [:1],
                ),
            )
            .update(denormalised_str=(
                F("user_username")
                + self.model.INFIX
                + F("capability_name")
            ))
        )


class Manager(models.Manager.from_queryset(QuerySet)):

    def can_created(self, pk):
        self.filter(pk=pk).denormalise_strs()


class Can(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    capability = models.ForeignKey(
        "capabilities.Capability",
        on_delete=models.CASCADE,
        related_name="capabilities",
    )

    INFIX = " can "
    denormalised_str = models.CharField(
        max_length=(
            foreign_model(user).username.field.max_length
            + CAPABILITY_NAME_LENGTH
            + len(INFIX)
        ),
        editable=False,
    )

    objects = Manager()

    class Meta:
        unique_together = [
            ("user", "capability"),
        ]

    def __str__(self):
        return self.denormalised_str
