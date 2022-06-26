from django.urls import path

from . import views

app_name = "people"

urlpatterns = [
    path("", views.ProfileListView.as_view(), name="profile_list"),
    path("<slug:slug>", views.ProfileDetailView.as_view(), name="profile_detail"),
]
