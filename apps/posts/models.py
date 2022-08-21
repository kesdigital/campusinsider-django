import os
from uuid import uuid4

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.core.models import SluggedModel, TimestampedModel
from apps.core.utils import compress_image

User = get_user_model()


class Tag(SluggedModel, TimestampedModel):
    tag_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    about = models.TextField()

    class Meta(TimestampedModel.Meta):
        db_table = "tag"


def upload_thumbnail_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join("thumbnails", f"{instance.post_id}{ext}")


class Post(TimestampedModel):
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

    post_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=160, unique=True)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to=upload_thumbnail_to)
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="posts")
    content = models.TextField()  #! change to rich text
    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)
    status = models.CharField(max_length=2, choices=ARTICLE_STATUSES, default=DRAFT)
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta(TimestampedModel.Meta):
        db_table = "post"
        permissions = [
            ("can_publish_a_post", "Can publish a post"),
            ("can_mark_post_as_featured", "Can mark post as featured"),
        ]

    def clean(self):
        if self.is_featured and self.status != self.PUBLISHED:
            raise ValidationError({"is_featured": _("Suspended, Draft or Unpublished posts can't be featured")})

        if self.status == self.DRAFT and self.published_at is not None:
            raise ValidationError({"published_at": _("Draft posts should not have a publication date.")})

        if self.status == self.PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()

    def save(self, *args, **kwargs):
        # optimize thumbnail
        try:
            optimized_thumbnail = compress_image(self.thumbnail)
        except Exception as e:
            print(e)
            print("Error occurred when optimizing thumbnail")
        else:
            self.thumbnail = optimized_thumbnail

        # generate slug
        if not self.slug:
            self.slug = slugify(self.title)
        super().full_clean()
        super().save(*args, **kwargs)

    @admin.display(
        boolean=True,
        ordering="published_at",
        description="Post is published",
    )
    def is_published(self):
        return self.status == self.PUBLISHED
