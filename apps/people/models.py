import os
import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.core.models import SluggedModel, TimestampedModel
from apps.core.utils import optimize_image


class Role(SluggedModel, TimestampedModel):
    role_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    about = models.TextField()

    class Meta(TimestampedModel.Meta):
        db_table = "role"


def upload_avatar_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join("avatars", f"{instance.profile_id}{ext}")


class Profile(TimestampedModel):
    """
    The owner of the profile doesn't need to be a user with login credentials, for example when we
    feature a profile, that profile doesn't have to be associated to an account owner. So this model won't
    be associated to the User model.
    """

    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=45, unique=True, blank=True)
    avatar = models.ImageField(upload_to=upload_avatar_to)
    bio = models.TextField()
    course = models.CharField(max_length=60, null=True, blank=True)
    date_of_birth = models.DateField(_("born on"), null=True, blank=True)
    campus = models.ForeignKey(
        to="campuses.Campus", on_delete=models.PROTECT, related_name="people", null=True, blank=True
    )
    # socials
    public_email = models.EmailField(_("the public email"), null=True, blank=True)
    twitter_url = models.URLField(_("link to twitter account"), null=True, blank=True)
    twitter_username = models.CharField(_("twitter handle"), max_length=20, null=True, blank=True)
    facebook_url = models.URLField(_("link to facebook account"), null=True, blank=True)
    facebook_username = models.CharField(max_length=20, null=True, blank=True)
    instagram_url = models.URLField(_("link to instagram account"), null=True, blank=True)
    instagram_username = models.CharField(max_length=20, null=True, blank=True)
    # roles
    main_role = models.ForeignKey(
        to="Role",
        on_delete=models.PROTECT,
        related_name="main_profiles",
        help_text="The main role of the profile's owner in relation to the website, ie Admin, Founder, Sponsor",
    )
    roles = models.ManyToManyField(to="Role", verbose_name="Other roles for this profile's owner", blank=True)

    class Meta(TimestampedModel.Meta):
        db_table = "profile"

    def __str__(self) -> str:
        return str(self.username)

    def save(self, *args, **kwargs):
        # optimize avatar
        try:
            optimized_avatar = optimize_image(self.avatar, width=150, height=150, method="thumb")
        except Exception as e:
            print(e)
            print("Error occurred when optimizing avatar")
        else:
            self.avatar = optimized_avatar

        # generate slug
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class FeaturedProfile(TimestampedModel):
    featured_profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(to="Profile", on_delete=models.CASCADE)

    class Meta(TimestampedModel.Meta):
        db_table = "featured_profile"

    def __str__(self):
        return f"Featuring {self.profile.username}"
