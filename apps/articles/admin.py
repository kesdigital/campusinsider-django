from django.contrib import admin

from .forms import ArticleForm
from .models import Article, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "is_featured")
    list_filter = ("status", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    form = ArticleForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "author",
                    "thumb_nail",
                    "content",
                    "tags",
                    "is_featured",
                    "status",
                    "published_at",
                ),
            },
        ),
    )
