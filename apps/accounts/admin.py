from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active", "is_superuser", "date_joined")
    list_filter = ("is_superuser", "is_staff", "is_active")
    ordering = ("email",)
    search_fields = ("email",)
    fieldsets = ((None, {"fields": ("email", "password", "is_staff", "is_active", "profile", "groups")}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active", "groups"),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super(UserAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            read_only_fields += ("is_staff", "is_superuser", "groups", "user_permissions")
        return read_only_fields
