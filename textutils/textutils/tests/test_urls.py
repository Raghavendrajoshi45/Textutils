from django.test import SimpleTestCase
from django.urls import reverse, resolve
from textutils.views import index , analyze

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_analyze_url_is_resolved(self):
        url = reverse('analyze')
        print(resolve(url))
        self.assertEquals(resolve(url).func, analyze)