from django.apps import AppConfig


class Capabilities(AppConfig):
    name = "capabilities"

    def ready(self):
        from .handlers import connect

        connect()
