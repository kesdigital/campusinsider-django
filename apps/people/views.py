from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Profile, FeaturedProfile


class ProfileListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        featured_profiles = FeaturedProfile.objects.select_related("profile")[:8]
        context = {"featured_profiles": featured_profiles}
        return render(request, "people/profile_list.html", context)


class ProfileDetailView(View):
    def get(self, request: HttpRequest, slug) -> HttpResponse:
        try:
            profile = Profile.objects.select_related("campus", "main_role").get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
        context = {"profile": profile}
        return render(request, "people/profile_detail.html", context)
