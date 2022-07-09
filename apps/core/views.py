from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from apps.posts.models import Post
from apps.profiles.models import FeaturedProfile


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        featured_profiles = FeaturedProfile.objects.select_related("profile")[:6]
        featured_posts = (
            Post.objects.select_related("author")
            .order_by("-published_at")
            .filter(is_featured=True, status=Post.PUBLISHED)[:3]
        )
        context = {"featured_profiles": featured_profiles, "featured_posts": featured_posts}
        return render(request, "core/home.html", context)
