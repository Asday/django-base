import pytest

from . import factories


@pytest.mark.parametrize("name", ["Can", "Capability", "Implication"])
@pytest.mark.django_db
def str_methods_work(name):
    instance = getattr(factories, name).create()

    str(instance)
