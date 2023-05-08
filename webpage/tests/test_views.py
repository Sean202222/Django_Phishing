from django.test import TestCase, Client
from django.urls import reverse

class TestViuews(TestCase):
    def test_phish1_get(self):
        client = Client()
        response = client.get(reverse('phish1'))
        
        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'phish1.html')
        