from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):
    def test_home_page_url(self):
        self.assertEqual(reverse("core:home"), "/", msg="URLs don't match")

    def test_home_view_response(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")


class TestAboutView(TestCase):
    def test_about_page_url(self):
        self.assertEqual(reverse("core:about"), "/about", msg="URLs don't match")

    def test_about_view_response(self):
        response = self.client.get(reverse("core:about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/about.html")
