from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

# from apps.articles.models import Article
# from apps.people.models import FeaturedProfile


# class HomeView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         featured_profiles = FeaturedProfile.objects.select_related("profile")[:6]
#         featured_articles = (
#             Article.objects.select_related("author")
#             .order_by("-published_at")
#             .filter(is_featured=True, status=Article.PUBLISHED)[:2]
#         )
#         context = {"featured_profiles": featured_profiles, "featured_articles": featured_articles}
#         return render(request, "core/home.html", context)


# class AboutView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         return render(request, "core/about.html")
