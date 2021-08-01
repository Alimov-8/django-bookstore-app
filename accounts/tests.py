from django.contrib.auth import get_user_model
from django.test import TestCase

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