from django.apps import apps
from django.db.models.signals import post_save, pre_delete


Can = apps.get_model("capabilities.Can")
Capability = apps.get_model("capabilities.Capability")
Implication = apps.get_model("capabilities.Implication")


def can_created(created, raw, instance, **kwargs):
    if not created or raw:
        return

    Can.objects.can_created(instance.pk)


def capability_created(created, raw, instance, **kwargs):
    if not created or raw:
        return

    Implication.objects.capability_created(instance)


def capability_deleted(instance, **kwargs):
    Implication.objects.capability_deleted(instance)


def implication_created(created, raw, instance, **kwargs):
    if not created or raw:
        return

    Implication.objects.implication_created(instance)


def implication_deleted(instance, **kwargs):
    Implication.objects.implication_deleted(instance.pk)


def connect():
    post_save.connect(can_created, sender="capabilities.Can")

    post_save.connect(capability_created, sender="capabilities.Capability")
    pre_delete.connect(capability_deleted, sender="capabilities.Capability")

    post_save.connect(implication_created, sender="capabilities.Implication")
    pre_delete.connect(implication_deleted, sender="capabilities.Implication")
