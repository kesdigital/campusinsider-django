import os
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from embed_video.fields import EmbedVideoField

from apps.core.models import SluggedModel, TimestampedModel


def upload_poster_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join("posters", f"{instance.on_tv_id}{ext}")


class Cinema(SluggedModel, TimestampedModel):
    cinema_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta(TimestampedModel.Meta):
        db_table = "cinema"


class Category(SluggedModel, TimestampedModel):
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta(TimestampedModel.Meta):
        db_table = "category"


class OnTV(TimestampedModel):
    MOVIE = "MOVIE"
    SERIE = "SERIE"

    OnTV_TYPES = [
        (MOVIE, "Movie"),
        (SERIE, "Serie"),
    ]
    on_tv_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=160, unique=True)
    on_tv_type = models.CharField(max_length=5, choices=OnTV_TYPES, default=MOVIE)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    poster = models.ImageField(upload_to=upload_poster_to)
    trailer = EmbedVideoField()
    about = models.TextField()
    rating = models.PositiveSmallIntegerField(
        help_text="The movie or serie rating in percentage",
        validators=[
            MinValueValidator(limit_value=0, message="Rating can't be less than 0%"),
            MaxValueValidator(limit_value=100, message="Rating can't be more than 100%"),
        ],
    )
    in_cinema = models.BooleanField(default=False)
    cinemas = models.ManyToManyField(to=Cinema, blank=True)
    categories = models.ManyToManyField(to=Category, blank=True)

    class Meta(TimestampedModel.Meta):
        db_table = "on_tv"

    def __str__(self) -> str:
        return str(self.name)

    def clean(self):
        if self.in_cinema and not self.cinemas:
            raise ValidationError({"in_cinema": _("If a movie is in cinema, then you must specify which cinemas")})

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().full_clean()
        super().save(*args, **kwargs)
