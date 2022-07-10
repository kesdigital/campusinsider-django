from django.contrib import admin

from .models import Cinema, Category, OnTV


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OnTV)
class OnTVAdmin(admin.ModelAdmin):
    pass
