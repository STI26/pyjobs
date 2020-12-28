from rest_framework.test import APITestCase

from dashboard.models import User
from ..models import Applicant, Resume


class ApplicantTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user_1',
            password='pass_1'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_applicant_without_data(self):
        response = self.client.post('/api/resumes/applicant/')
        self.assertEqual(response.status_code, 400)

    def test_create_applicant_with_correct_data(self):
        data = {'bio': 'some description', 'date_of_birth': '2000-01-01'}
        response = self.client.post('/api/resumes/applicant/', data, 'json')
        self.assertEqual(response.data['id'], self.user.applicant.pk)
        self.assertEqual(response.status_code, 201)


class ResumeTestCase(APITestCase):
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

    def test_create_resume_without_profile(self):
        data = {'position': 'python developer'}
        response = self.client.post('/api/resumes/resume/', data, 'json')
        self.assertEqual(response.status_code, 400)

    def test_create_resume_with_correct_data(self):
        Applicant.objects.create(profile=self.user, bio='description')

        data = {'position': 'python developer'}
        response = self.client.post('/api/resumes/resume/', data, 'json')

        self.assertEqual(response.data['owner_info']['user_id'], self.user.pk)
        self.assertEqual(response.status_code, 201)

    def test_update_another_user_resume(self):
        applicant = Applicant.objects.create(profile=self.another_user,
                                             bio='description')
        Resume.objects.create(owner=applicant, position='python developer')

        data = {'skills': [{'tag': 'django'}]}
        response = self.client.patch('/api/resumes/resume/1/', data, 'json')

        self.assertEqual(response.status_code, 403)

    def test_update_your_resume(self):
        applicant = Applicant.objects.create(profile=self.user,
                                             bio='description')
        Resume.objects.create(owner=applicant, position='python developer')

        data = {'skills': [{'tag': 'django'}]}
        response = self.client.patch('/api/resumes/resume/1/', data, 'json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['skills'][0]['tag'], 'django')
