from contextlib import contextmanager
import math
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


@contextmanager
def override(target, attr, value):
    overridden_value = getattr(target, attr)
    setattr(target, attr, value)

    try:
        yield None
    finally:
        setattr(target, attr, overridden_value)


def tanh_timeout(asymptote, max_tries):
    for i in range(max_tries):
        yield math.tanh(i / 5) * asymptote


class Command(BaseCommand):
    requires_system_checks = []

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")

        for seconds in tanh_timeout(5, 5):
            try:
                with override(self.stdout, "write", lambda *args: None):
                    self.check_migrations()
            except OperationalError:
                pass  # Not ready yet.
            else:  # nobreak
                self.stdout.write("Database responded.")

                return

            time.sleep(seconds)

        raise TimeoutError("max tries exceeded")
