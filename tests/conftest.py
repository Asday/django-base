from factory import Faker

from .capabilities.factories import CapabilitiesProvider


Faker.add_provider(CapabilitiesProvider)

collect_ignore_glob = ["*/factories.py"]
