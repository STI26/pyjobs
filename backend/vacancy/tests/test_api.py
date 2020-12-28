from rest_framework.test import APITestCase

from dashboard.models import User
from ..models import Company, Vacancy


class CompanyTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user',
            password='pass'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_company_without_data(self):
        response = self.client.post('/api/vacancies/company/')
        self.assertEqual(response.status_code, 400)

    def test_create_company_with_correct_data(self):
        data = {'name': 'The Company', 'description': 'it company'}
        response = self.client.post('/api/vacancies/company/', data, 'json')
        self.assertEqual(response.data['id'], self.user.companies.first().pk)
        self.assertEqual(response.status_code, 201)


class VacancyTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user',
            password='pass'
        )
        self.another_user = User.objects.create(
            username='another_user',
            password='another_pass'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_vacancy_without_company(self):
        data = {'position': 'python developer', 'description': 'pass'}
        response = self.client.post('/api/vacancies/vacancy/', data, 'json')
        self.assertEqual(response.status_code, 400)

    def test_create_vacancy_with_correct_data(self):
        company = Company.objects.create(owner=self.user, name='The Company',
                                         description='it company')

        data = {'company': company.pk,
                'position': 'python developer',
                'description': 'pass'}
        response = self.client.post('/api/vacancies/vacancy/', data, 'json')

        self.assertEqual(response.data['company_info']['user_id'], self.user.pk)
        self.assertEqual(response.status_code, 201)

    def test_update_another_user_vacancy(self):
        company = Company.objects.create(owner=self.another_user,
                                         name='The Company',
                                         description='it company')
        Vacancy.objects.create(company=company, position='python developer')

        data = {'salary': 1000}
        response = self.client.patch('/api/vacancies/vacancy/1/', data, 'json')

        self.assertEqual(response.status_code, 403)

    def test_update_your_vacancy(self):
        company = Company.objects.create(owner=self.user, name='The Company',
                                         description='it company')
        Vacancy.objects.create(company=company, position='python developer')

        data = {'salary': 1000}
        response = self.client.patch('/api/vacancies/vacancy/1/', data, 'json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['salary'], 1000)
