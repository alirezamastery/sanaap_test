from django.urls import reverse
from rest_framework.test import APITransactionTestCase


class TestTaskAPI(APITransactionTestCase):
    reset_sequences = True
    fixtures = [
        'task_manager/tests/api/fixtures/user.json'
    ]

    def setUp(self):
        jwt_url = reverse('users_public:token_obtain_pair')

        self.client_401 = self.client_class()
        self.client_admin = self.client_class()
        self.client_2 = self.client_class()
        self.client_3 = self.client_class()

        res_admin = self.client_admin.post(jwt_url, data={
            'mobile':   '09120000111',
            'password': '123456',
        })
        self.client_admin.credentials(HTTP_AUTHORIZATION=f'Bearer {res_admin.data["access"]}')

        res_2 = self.client_2.post(jwt_url, data={
            'mobile':   '09120000222',
            'password': '123456',
        })
        self.client_2.credentials(HTTP_AUTHORIZATION=f'Bearer {res_2.data["access"]}')

        res_3 = self.client_3.post(jwt_url, data={
            'mobile':   '09120000333',
            'password': '123456',
        })
        self.client_3.credentials(HTTP_AUTHORIZATION=f'Bearer {res_3.data["access"]}')

        self.url_base = reverse('task_public:tasks-list')

    def test_auth(self):
        res = self.client_401.get(self.url_base)
        self.assertEqual(res.status_code, 401)

        payload = {
            'title':  'test',
            'status': 'RUNNING'
        }
        res = self.client_401.post(self.url_base, data=payload)
        self.assertEqual(res.status_code, 401)

    def test_crud(self):
        payload = {
            'title':  'test',
            'status': 'RUNNING'
        }
        res = self.client_2.post(self.url_base, data=payload)
        self.assertEqual(res.status_code, 201)
        task_id = res.data['id']
        task_url = f'{self.url_base}{task_id}/'

        res = self.client_2.get(task_url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['title'], payload['title'])
        self.assertEqual(res.data['status'], payload['status'])

        new_stat = 'COMPLETED'
        res = self.client_2.patch(task_url, data={'status': new_stat})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['status'], new_stat)

        res = self.client_2.delete(task_url)
        self.assertEqual(res.status_code, 204)

    def test_permissions(self):
        payload = {
            'title':  'test',
            'status': 'RUNNING'
        }
        res = self.client_2.post(self.url_base, data=payload)
        task_id = res.data['id']
        task_url = f'{self.url_base}{task_id}/'

        res = self.client_admin.get(task_url)
        self.assertEqual(res.status_code, 403)

        res = self.client_3.patch(task_url, data={'title': 'task test'})
        self.assertEqual(res.status_code, 403)
