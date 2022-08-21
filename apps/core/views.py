from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from apps.entertainment.models import OnTV
from apps.posts.models import Post
from apps.profiles.models import FeaturedProfile


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        featured_profiles = FeaturedProfile.objects.select_related("profile")[:6]
        on_tv = OnTV.objects.prefetch_related("cinemas")[:12]
        featured_posts = (
            Post.objects.select_related("author")
            .order_by("-published_at")
            .filter(is_featured=True, status=Post.PUBLISHED)[:3]
        )
        context = {"featured_profiles": featured_profiles, "featured_posts": featured_posts, "on_tv": on_tv}
        return render(request, "core/home.html", context)
