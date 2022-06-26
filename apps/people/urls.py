from django.urls import path

from . import views

app_name = "people"

urlpatterns = [path("", views.ProfileListView.as_view(), name="profile_list")]
