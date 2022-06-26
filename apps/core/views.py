from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from apps.people.models import FeaturedProfile


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        featured_profiles = FeaturedProfile.objects.select_related("profile")[:6]
        context = {"featured_profiles": featured_profiles}
        return render(request, "core/home.html", context)


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "core/about.html")
