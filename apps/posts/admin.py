from django.contrib import admin

from .forms import PostForm
from .models import Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "is_featured")
    list_filter = ("status", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
    form = PostForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "author",
                    "thumbnail",
                    "content",
                    "tags",
                    "is_featured",
                    "status",
                    "published_at",
                ),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super(PostAdmin, self).get_readonly_fields(request, obj)
        if not request.user.has_perm("apps.posts.can_publish_a_post"):
            read_only_fields += ("status",)
        if not request.user.has_perm("apps.posts.can_mark_post_as_featured"):
            read_only_fields += ("is_featured",)
        return read_only_fields
