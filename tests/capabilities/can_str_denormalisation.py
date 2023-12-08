import pytest

from .factories import Can


@pytest.mark.django_db
def works_on_creation():
    can = Can.create()

    assert can.user.username in can.denormalised_str
    assert can.capability.name in can.denormalised_str


# @pytest.mark.db
# def updates():
#     user =
