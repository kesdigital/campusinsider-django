import uuid

from django.db import models

from apps.core.models import SluggedModel, TimestampedModel


class Campus(SluggedModel, TimestampedModel):
    campus_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(TimestampedModel.Meta):
        db_table = "campus"
        verbose_name = "campus"
        verbose_name_plural = "campuses"
