from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Profile


class ProfileDetailView(View):
    def get(self, request: HttpRequest, slug) -> HttpResponse:
        try:
            profile = Profile.objects.get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
        context = {"profile": profile}
        return render(request, "profiles/profile_detail.html", context)
