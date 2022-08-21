from django.urls import path

from . import views

app_name = "entertainment"

urlpatterns = [path("movies/<slug:slug>", views.ShowDetail.as_view(), name="show_detail")]
