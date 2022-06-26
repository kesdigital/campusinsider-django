from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View


class ProfileListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "people/profile_list.html")
