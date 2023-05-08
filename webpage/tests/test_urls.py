from django.test import SimpleTestCase
from django.urls import reverse, resolve
from webpage.views import index

class TestUrls(SimpleTestCase):
    
    def test_phish1_url(self):
        path = reverse('index')
        self.assertAlmostEqual(resolve(path).func, index)
    
    
    
 