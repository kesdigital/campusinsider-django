from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Post, Tag


class PostListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        tags = Tag.objects.all()
        posts = Post.objects.filter(status=Post.PUBLISHED).select_related("author").prefetch_related("tags")
        context = {"posts": posts, "tags": tags}
        return render(request, "posts/post_list.html", context)
