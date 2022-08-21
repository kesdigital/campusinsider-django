from django.contrib import admin

from .models import Campus


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super(CampusAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            read_only_fields += ("name", "slug")
        return read_only_fields
