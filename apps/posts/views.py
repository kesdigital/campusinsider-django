from django.shortcuts import render

from django.views import View
from django.http import HttpRequest, HttpResponse

from .models import Post


class PostListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        posts = Post.objects.filter(status=Post.PUBLISHED).select_related("tags", "author")
        context = {"posts": posts}
        return render(request, "posts/post_list.html", context)
