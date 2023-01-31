
from django.test import TestCase
from django.urls import reverse
from users.models import Users


class CRUD_user_test(TestCase):

    def setUp(self):
        Users.objects.create_user(
            username='testuser',
            first_name='1test@email.com',
            password='qwerty'
        )
        self.user = Users.objects.get(pk=1)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.first_name, '1test@email.com')

    def test_index(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.username, 'testuser')

    # CREATE - Регистрация нового пользователя
    def test_create_user(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'john_smith', 'password': '12345'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_read_user(self):
        response = self.client.post(reverse('user_login'),
                                    {'username': 'ivan_ivanov',
                                     'password': 'qwerty'})
        self.assertEqual(response.status_code, 200)

    # UPDATE - обновленние данных пользователя
    def test_update_user(self):
        self.client.login(username='ivan_ivanov', password='qwerty')
        response = self.client.post(reverse('update_user',
                                            kwargs={'pk': self.user.pk}),
                                    {'first_name': 'Ivan',
                                     'last_name': 'Ivanov',
                                     'email': 'ivanivanov@gmail.com'})
        self.assertEqual(response.status_code, 302)

    # DELETE - удаления пользователя
    def test_user_delete_view(self):  # новое
        response = self.client.post(
            reverse('delete_user', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
