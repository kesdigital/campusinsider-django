from django.contrib import admin

from .models import Profile, FeaturedProfile, Photo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "profile_type")
    list_filter = ("profile_type",)


@admin.register(FeaturedProfile)
class FeaturedProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
