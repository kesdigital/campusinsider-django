import shutil
import tempfile
from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings
from django.utils import timezone

from apps.core.utils import get_test_image_file

from ..models import Article, Tag

User = get_user_model()

MEDIA_ROOT = tempfile.gettempdir()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestArticleModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # run once to setup unmodified test data for all methods
        Tag.objects.create(name="fashion", about="All about fashion")
        Tag.objects.create(name="news", about="This is news")
        User.objects.create_user(email="william@shakespear.com", password="testpas256")
        cls.william = User.objects.get(email="william@shakespear.com")

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_articles_get_an_auto_slug(self):
        test_article = Article.objects.create(
            title="Test article one",
            author=self.william,
            thumb_nail=get_test_image_file(width=600, height=300),
            content="This is a test article",
            status=Article.DRAFT,
        )
        self.assertEqual(test_article.slug, "test-article-one")

    def test_articles_are_unique(self):
        with self.assertRaises(ValidationError):
            Article.objects.create(
                title="Test article one",
                author=self.william,
                thumb_nail=get_test_image_file(width=600, height=300),
                content="This is a test article",
                status=Article.DRAFT,
            )
            Article.objects.create(
                title="Test article one",
                author=self.william,
                thumb_nail=get_test_image_file(width=600, height=300),
                content="This is a test article",
                status=Article.DRAFT,
            )

    def test_cant_feature_an_unpublished_article(self):
        with self.assertRaises(ValidationError):
            Article.objects.create(
                title="Test article one",
                author=self.william,
                thumb_nail=get_test_image_file(width=600, height=300),
                content="This is a test article",
                status=Article.DRAFT,
                is_featured=True,
            )

    def test_published_articles_without_a_date_get_an_auto_date(self):
        test_article_one = Article.objects.create(
            title="Test article one",
            author=self.william,
            thumb_nail=get_test_image_file(width=600, height=300),
            content="This is a test article",
            status=Article.PUBLISHED,
            is_featured=True,
        )
        self.assertIsNotNone(test_article_one.published_at)
        self.assertTrue(isinstance(test_article_one.published_at, datetime))

    def test_draft_articles_with_a_published_at_raise_an_error(self):
        with self.assertRaises(ValidationError):
            Article.objects.create(
                title="Test article one",
                author=self.william,
                thumb_nail=get_test_image_file(width=600, height=300),
                content="This is a test article",
                status=Article.DRAFT,
                published_at=timezone.now(),
            )
