from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserManager(TestCase):
    def test_create_user(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(email="user@email.com", password="testpas256")
        self.assertEqual(user.email, "user@email.com", msg="user emails don't match")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            UserModel.objects.create_user()
        with self.assertRaises(TypeError):
            UserModel.objects.create_user(email="")
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(email="", password="foobar")

    def test_create_superuser(self):
        UserModel = get_user_model()
        super_user = UserModel.objects.create_superuser(email="super@email.com", password="testpas256")
        self.assertEqual(super_user.email, "super@email.com", msg="user emails don't match")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        try:
            self.assertIsNone(super_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            UserModel.objects.create_superuser(email="", password="foobar", is_superuser=False)
