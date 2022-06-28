from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
    def test_url_available_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_template_name_correct(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp, "home.html")
    def test_template_content(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, "Homepage")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        resp = self.client.get("/about")
        self.assertEqual(resp.status_code, 200)
    def test_url_available_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
    def test_template_name_correct(self):
        resp = self.client.get(reverse('about'))
        self.assertTemplateUsed(resp, "about.html")
    def test_template_content(self):
        resp = self.client.get(reverse('about'))
        self.assertContains(resp, "About Page")
