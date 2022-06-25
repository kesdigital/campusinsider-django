import shutil
import tempfile

from django.test import TestCase, override_settings

from apps.core.utils import get_test_image_file
from apps.people.models import Profile, Role

from ..models import Campus

MEDIA_ROOT = tempfile.gettempdir()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestCampusModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # run once to setup unmodified test data for all methods
        harvard = Campus.objects.create(name="Harvard")
        cambridge = Campus.objects.create(name="Cambridge")
        student = Role.objects.create(name="Student")
        Profile.objects.create(
            name="Bill Gates", main_role=student, campus=harvard, bio="Founded Microsoft", avatar=get_test_image_file()
        )
        Profile.objects.create(
            name="Steve Jobs", main_role=student, campus=harvard, bio="Founded Apple", avatar=get_test_image_file()
        )
        Profile.objects.create(
            name="Allan Turing", main_role=student, campus=cambridge, bio="Codebreaker", avatar=get_test_image_file()
        )

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_created_campuses(self):
        campus_count = Campus.objects.count()
        cambridge = Campus.objects.get(name="Cambridge")
        harvard = Campus.objects.get(name="Harvard")
        self.assertEqual(campus_count, 2)
        self.assertQuerysetEqual(Campus.objects.all(), [cambridge, harvard])

    def test_auto_slug(self):
        harvard = Campus.objects.get(name="Harvard")
        self.assertEqual(harvard.slug, "harvard")
        cambridge = Campus.objects.get(name="Cambridge")
        self.assertEqual(cambridge.slug, "cambridge")

    def test_reverse_relationship_with_campus_model(self):
        bill_gates = Profile.objects.get(name="Bill Gates")
        steve_jobs = Profile.objects.get(name="Steve Jobs")
        allan_turing = Profile.objects.get(name="Allan Turing")
        harvard = Campus.objects.get(name="Harvard")
        cambridge = Campus.objects.get(name="Cambridge")
        self.assertTrue(hasattr(harvard, "people"))
        self.assertQuerysetEqual(harvard.people.all(), [steve_jobs, bill_gates])
        self.assertQuerysetEqual(cambridge.people.all(), [allan_turing])
        self.assertEqual(harvard.people.count(), 2)

    def test_campus_queryset_default_ordering(self):
        """The campus default queryset is order in descending order on the created_at field"""
        cambridge = Campus.objects.get(name="Cambridge")
        harvard = Campus.objects.get(name="Harvard")
        self.assertQuerysetEqual(Campus.objects.all(), [cambridge, harvard], msg="Campus QuerySet out of order")
