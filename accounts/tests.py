from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve 
from .forms import CustomUserCreationForm 
from .views import SignupPageView

# Create your tests here.


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()

        user = User.objects.create_user(
            username='user',
            email='user@email.com',
            password='userpass123'
        )
        self.assertEqual(user.username, 'user')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(get_user_model().objects.all().count(), 1)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superuser',
            email='superuser@email.com',
            password='superuserpass123'
        )
        self.assertEqual(admin_user.username, 'superuser')
        self.assertEqual(admin_user.email, 'superuser@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


# Do not need to test log in and log out features since those are built into Django and
# already have tests. We do need to test our sign up functionality though!

class SignupTests(TestCase): 
    username = 'newuser'
    email = 'newuser@email.com'
    
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')
        
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                        [0].email, self.email)


# class SignupPageTests(TestCase): 
#     # if test suite seems sluggish a potential
#     # optimization to look into is using setUpTestData()
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)

#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'registration/signup.html')
#         self.assertContains(self.response, 'Sign Up')
#         self.assertNotContains(
#             self.response, 'Hi there! I should not be on the page.')

#     def test_signup_form(self):  
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')

#     def test_signup_view(self):
#         view = resolve('/accounts/signup/')
#         self.assertEqual(
#             view.func.__name__,
#             SignupPageView.as_view().__name__
#         )
