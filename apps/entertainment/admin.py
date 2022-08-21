from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import Category, Cinema, OnTV


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OnTV)
class OnTVAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
