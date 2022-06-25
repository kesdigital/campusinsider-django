from django.contrib import admin

from .models import Campus


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
