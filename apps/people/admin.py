from django.contrib import admin

from .forms import ProfileForm
from .models import FeaturedProfile, Profile, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "main_role")
    form = ProfileForm
    fieldsets = (
        (
            "Info",
            {
                "fields": ("name", "slug", "avatar", "campus", "date_of_birth", "course", "bio"),
            },
        ),
        (
            "Social",
            {
                "fields": (
                    "public_email",
                    "twitter_url",
                    "twitter_username",
                    "instagram_url",
                    "instagram_username",
                    "facebook_url",
                    "facebook_username",
                )
            },
        ),
        ("Roles", {"fields": ("main_role", "roles")}),
    )


@admin.register(FeaturedProfile)
class FeaturedProfileAdmin(admin.ModelAdmin):
    pass
