from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Profile


class ProfileListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "people/profile_list.html")


class ProfileDetailView(View):
    def get(self, request: HttpRequest, slug) -> HttpResponse:
        try:
            profile = Profile.objects.select_related("campus", "main_role").get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
        context = {"profile": profile}
        return render(request, "people/profile_detail.html", context)
