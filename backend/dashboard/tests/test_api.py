from rest_framework.test import APITestCase

from ..models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='pass'
        )

    def test_user_login_without_data(self):
        response = self.client.post('/login/')
        self.assertEqual(response.status_code, 401)

    def test_user_login_with_correct_data(self):
        data = {'username': 'user', 'password': 'pass'}
        response = self.client.post('/login/', data, 'json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'user')

    def test_user_register_without_confirm(self):
        data = {
            'username': 'another_user',
            'password': 'another_pass'
        }
        response = self.client.post('/register/', data, 'json')
        self.assertEqual(response.status_code, 401)

    def test_user_register_with_correct_data(self):
        data = {
            'username': 'another_user',
            'password': 'another_pass',
            'confirm': 'another_pass'
        }
        response = self.client.post('/register/', data, 'json')
        self.assertEqual(response.data['username'], 'another_user')
        self.assertEqual(response.status_code, 201)
