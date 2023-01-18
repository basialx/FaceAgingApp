from django.test import TestCase, Client
from django.urls import reverse

from Image.models import Image

class ViewsTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.response = self.c.post('/login/', {'username': 'john', 'password': 'smith'})

    def test(self):
        self.assertEqual(self.response.status_code, 200)
        self.response = self.c.get('home')