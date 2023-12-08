from django.apps import apps
from django.db import models
from django.db.models import F, OuterRef, Subquery

from .constants import CAPABILITY_NAME_LENGTH


class QuerySet(models.QuerySet):

    def denormalise_strs(self):
        Capability = apps.get_model("capabilities.Capability")

        (
            self
            .select_related("capability", "implies")
            .annotate(
                capability_name=Subquery(
                    Capability.objects
                    .filter(pk=OuterRef("capability_id"))
                    .values("name")
                    [:1],
                ),
                implies_name=Subquery(
                    Capability.objects
                    .filter(pk=OuterRef("implies_id"))
                    .values("name")
                    [:1],
                ),
            )
            .update(denormalised_str=(
                F("capability_name")
                + self.model.INFIX
                + F("implies_name")
            ))
        )


class Manager(models.Manager.from_queryset(QuerySet)):

    def capability_created(self, capability):
        self.model.objects.create(capability=capability, implies=capability)

    def capability_deleted(self, capability):
        (
            (capability.implicators.all() | capability.implications.all())
            .distinct()
            .update(references=F("references") - 1)
        )

        self.filter(references=0).delete()

    def implication_created(self, implication):
        self.filter(pk=implication.pk).denormalise_strs()

    def implication_deleted(self, implication_pk):
        pass


class Implication(models.Model):
    # Raw string to ignore the invalid escape sequence `\ `.
    r"""
    Implements set of directed acyclic graphs by means of a closure
    table describing paths, for query performance reasons.

    Paths through the graphs are reference counted.

    `Implication`s are the paths through the graphs, and `Capability`s
    are the nodes.

    Automatic handling of creation and deletion of both `Capability`s
    and `Implication`s is handled by signal handlers.

    Without reference counting, paths to a non-direct descendent become
    ambiguous, so in the case of the following graph with edges facing
    downwards, represented by the table to its right, deleting `b` may
    or may not require deletion of implication `(a, c)`.

        a    (a, a)
        | \  (b, b) x
        b |  (a, b) x
        | /  (c, c)
        c    (b, c)
             (a, c) ?

    With reference counting, the `Implication`s become the following:

        (a, a, 1)
        (b, b, 1)
        (a, b, 1)
        (c, c, 1)
        (b, c, 1)
        (a, c, 2)

    The `Implication`s marked for deletion as a result of `b` being
    deleted instead have their reference count decremented, and then any
    with 0 references can be deleted.  The reference count can be
    thought of as the amount of unique paths through the graph there are
    for the given `Implication`.
    """
    capability = models.ForeignKey(
        "capabilities.Capability",
        on_delete=models.PROTECT,
        related_name="implicators",
    )
    implies = models.ForeignKey(
        "capabilities.Capability",
        on_delete=models.PROTECT,
        related_name="implications",
    )
    references = models.PositiveIntegerField(default=1)

    INFIX = " implies "
    denormalised_str = models.CharField(
        max_length=(
            CAPABILITY_NAME_LENGTH
            + CAPABILITY_NAME_LENGTH
            + len(INFIX)
        ),
        editable=False,
    )

    objects = Manager()

    class Meta:
        unique_together = [
            ("capability", "implies"),
        ]

    def __str__(self):
        return self.denormalised_str
