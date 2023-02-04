from django.test import TestCase
from django.urls import reverse
from users.models import Users

import os
import json

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.settings import FIXTURE_DIRS
from users.forms import RegisterUserForm
from django.utils.translation import gettext_lazy as _


class CrudUsertest(TestCase):
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.login_url = reverse_lazy('user_login')
        self.create_url = reverse_lazy('register')
        self.home = reverse_lazy('home')
        self.update_pk_1 = reverse_lazy('update_user', kwargs={'pk': 1})
        self.delete_pk_1 = reverse_lazy('delete_user', kwargs={'pk': 1})
        # self.update_pk_1 = reverse_lazy('update_user', kwargs = {'pk': 1})
        self.users = Users.objects.all()
        self.user1 = Users.objects.get(pk=1)
        self.user2 = Users.objects.get(pk=2)
        self.user3 = Users.objects.get(pk=3)

    # def setUp(self):
    #     Users.objects.create_user(
    #         username='testuser',
    #         first_name='1test@email.com',
    #         password='qwerty'
    #     )
    #     self.user = Users.objects.get(pk=1)self.

    def test_open_register(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(self.user.first_name, '')

    # def test_index(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(self.user.username, 'testuser')
    #
    # # CREATE - Регистрация нового пользователя
    # def test_create_user(self):
    #     response = self.client.post(reverse('register'),
    #                                 {'username': 'john_smith', 'password': '12345'}, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_read_user(self):
    #     response = self.client.post(reverse('user_login'),
    #                                 {'username': 'ivan_ivanov',
    #                                  'password': 'qwerty'})
    #     self.assertEqual(response.status_code, 200)
    #
    # # UPDATE - обновленние данных пользователя
    # def test_update_user(self):
    #     self.client.login(username='ivan_ivanov', password='qwerty')
    #     response = self.client.post(reverse('update_user',
    #                                         kwargs={'pk': self.user.pk}),
    #                                 {'first_name': 'Ivan',
    #                                  'last_name': 'Ivanov',
    #                                  'email': 'ivanivanov@gmail.com'})
    #     self.assertEqual(response.status_code, 302)
    #
    # # DELETE - удаления пользователя
    # def test_user_delete_view(self):  # новое
    #     response = self.client.post(
    #         reverse('delete_user', kwargs={'pk': self.user.pk}))
    #     self.assertEqual(response.status_code, 302)
