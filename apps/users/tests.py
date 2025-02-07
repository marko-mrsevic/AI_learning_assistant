from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create_user(email='test@example.com', password='testpass')

    def test_create_user(self):
        user = self.User.objects.create_user(email='test1@example.com', password='testpass1')
        self.assertEqual(user.email, "test1@example.com")
        self.assertTrue(user.check_password("testpass1"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin = self.User.objects.create_superuser(email="admin@example.com", password="adminpass")
        self.assertEqual(admin.email, "admin@example.com")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
