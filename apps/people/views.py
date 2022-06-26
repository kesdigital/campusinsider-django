from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Profile


class ProfileListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "people/profile_list.html")


class ProfileDetailView(View):
    def get(self, request: HttpRequest, slug) -> HttpResponse:
        profile = get_object_or_404(Profile, slug=slug)
        context = {"profile": profile}
        return render(request, "people/profile_detail.html", context)
