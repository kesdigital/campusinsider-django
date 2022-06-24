from django.conf import settings
from django.test import SimpleTestCase


class TestSettings(SimpleTestCase):
    def test_loaded_admins(self):
        self.assertTrue(hasattr(settings, "ADMINS"))
        self.assertTrue(isinstance(settings.ADMINS, list))
        self.assertTrue(isinstance(settings.ADMINS[0], tuple))

    def test_allowed_hosts(self):
        self.assertTrue(hasattr(settings, "ALLOWED_HOSTS"))
        self.assertTrue(isinstance(settings.ALLOWED_HOSTS, list))
