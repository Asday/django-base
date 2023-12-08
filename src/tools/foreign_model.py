from django.apps import apps


def foreign_model(fkey):
    return apps.get_model(fkey.remote_field.model, require_ready=False)
