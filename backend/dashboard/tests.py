from django.test import SimpleTestCase
from django.urls import resolve, reverse

from . import views


class HomeUrlTests(SimpleTestCase):
    def test_home_url_reverses_to_root(self):
        self.assertEqual(reverse("home"), "/")

    def test_root_url_resolves_to_home_view(self):
        match = resolve("/")
        self.assertEqual(match.func, views.home)
        self.assertEqual(match.url_name, "home")


class HomeViewTests(SimpleTestCase):
    def test_home_returns_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_uses_expected_templates(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "dashboard/home.html")
        self.assertTemplateUsed(response, "dashboard/base.html")

    def test_home_renders_dashboard_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Dashboard")
        self.assertContains(response, "QFM")
        self.assertContains(response, "Recent Activity")

    def test_home_only_allows_get(self):
        # The view is not decorated to reject other methods, but render
        # should still succeed for a HEAD request (no body).
        response = self.client.head(reverse("home"))
        self.assertEqual(response.status_code, 200)
