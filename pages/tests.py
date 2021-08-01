from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView 

# Create your tests here.

class HomePageTests(SimpleTestCase):
    # setUp
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # Testing URLs
    def test_homepage_status_code(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        # response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)
    
    # Testing Template
    def test_homepage_template(self): 
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    # Testing HTML
    def test_homepage_contains_correct_html(self): # new
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self): 
        # response = self.client.get('/')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    # Resolve
    def test_homepage_url_resolves_homepageview(self): 
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )