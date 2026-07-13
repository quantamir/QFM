from django.test import SimpleTestCase
from django.urls import resolve


class UrlConfTests(SimpleTestCase):
    def test_admin_url_is_registered(self):
        match = resolve("/admin/")
        self.assertEqual(match.app_name, "admin")

    def test_root_url_is_included_from_dashboard(self):
        match = resolve("/")
        self.assertEqual(match.url_name, "home")


class WsgiTests(SimpleTestCase):
    def test_wsgi_application_is_callable(self):
        from config.wsgi import application

        self.assertTrue(callable(application))


class AsgiTests(SimpleTestCase):
    def test_asgi_application_is_callable(self):
        from config.asgi import application

        self.assertTrue(callable(application))
