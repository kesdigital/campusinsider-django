from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

from .models import OnTV


class ShowDetail(View):
    def get(self, request: HttpRequest, slug) -> HttpResponse:
        show = OnTV.objects.get(slug=slug)
        context = {"show": show}
        return render(request, "entertainment/show_detail.html", context)
