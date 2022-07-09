import os
import uuid

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.core.models import SluggedModel, TimestampedModel
from apps.core.utils import optimize_image

User = get_user_model()


class Tag(SluggedModel, TimestampedModel):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    about = models.TextField()

    class Meta(TimestampedModel.Meta):
        db_table = "tag"


def upload_thumb_nail_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join("thumb_nails", f"{instance.article_id}{ext}")


class Article(TimestampedModel):
    DRAFT = "DR"
    PUBLISHED = "PB"  # public
    SUSPENDED = "SP"
    UNPUBLISHED = "UN"  # public but not available in the articles list

    ARTICLE_STATUSES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
        (SUSPENDED, "Suspended"),
        (UNPUBLISHED, "Unpublished"),
    ]

    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=160, unique=True)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    thumb_nail = models.ImageField(upload_to=upload_thumb_nail_to)  #! change me to thumbnail
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="articles")
    content = models.TextField()  #! change to rich text
    tags = models.ManyToManyField(to=Tag, related_name="articles")  #! add blank=True
    status = models.CharField(max_length=2, choices=ARTICLE_STATUSES)
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta(TimestampedModel.Meta):
        db_table = "article"
        permissions = [
            ("can_publish_an_article", "Can publish an article"),
            ("can_mark_article_as_featured", "Can mark article as featured"),
        ]

    def __str__(self):
        return str(self.title)

    def clean(self):
        if self.is_featured and self.status != self.PUBLISHED:
            raise ValidationError({"is_featured": _("Suspended, Draft or stale articles can't be featured")})

        if self.status == self.DRAFT and self.published_at is not None:
            # Don't allow draft articles to have a published_at.
            raise ValidationError({"published_at": _("Draft articles should not have a publication date.")})

        if self.status == self.PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()

    def save(self, *args, **kwargs):
        # optimize thumbnail
        try:
            optimized_thumb_nail = optimize_image(self.thumb_nail, width=600, height=300, method="cover")
        except Exception as e:
            print(e)
            print("Error occurred when optimizing thumbnail")
        else:
            self.thumb_nail = optimized_thumb_nail

        # generate slug
        if not self.slug:
            self.slug = slugify(self.title)
        super().full_clean()
        super().save(*args, **kwargs)

    @admin.display(
        boolean=True,
        ordering="published_at",
        description="Article is published",
    )
    def is_published(self):
        return self.status == self.PUBLISHED
