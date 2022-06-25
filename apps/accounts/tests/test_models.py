import shutil
import tempfile

from django.test import TestCase, override_settings

from apps.campuses.models import Campus
from apps.core.utils import get_test_image_file
from apps.people.models import Profile, Role

from ..models import User

MEDIA_ROOT = tempfile.gettempdir()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # run once to setup unmodified test data for all methods
        cambridge = Campus.objects.create(name="Cambridge")
        sponsor = Role.objects.create(name="Sponsor")
        benedict_profile = Profile.objects.create(
            name="Benedict Cumberbatch",
            main_role=sponsor,
            campus=cambridge,
            bio="British actor",
            avatar=get_test_image_file(),
        )
        benedict = User.objects.create_user(
            email="benedict@cumberbatch", password="testpas256", profile=benedict_profile
        )

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_user_with_profile(self):
        benedict = User.objects.get(email="benedict@cumberbatch")
        benedict_profile = benedict.profile
        self.assertEqual(benedict_profile.name, "Benedict Cumberbatch")
        self.assertEqual(benedict_profile.bio, "British actor")
