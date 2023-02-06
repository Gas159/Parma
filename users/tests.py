from django.test import TestCase
from django.urls import reverse
from users.models import Users
import os
import json
from django.urls import reverse_lazy
from task_manager.settings import FIXTURE_DIRS


class CrudUsertest(TestCase):
    ''' Dont forget your doc string :)'''
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.login_url = reverse_lazy('user_login')
        self.create_url = reverse_lazy('register')
        self.home = reverse_lazy('home')
        self.update_pk_1 = reverse_lazy('update_user', kwargs={'pk': 1})
        self.delete_pk_1 = reverse_lazy('delete_user', kwargs={'pk': 1})
        self.update_pk_2 = reverse_lazy('update_user', kwargs={'pk': 2})
        self.users = Users.objects.all()
        self.user1 = Users.objects.get(pk=1)
        self.user2 = Users.objects.get(pk=2)
        self.user3 = Users.objects.get(pk=3)
        with open(os.path.join(FIXTURE_DIRS[0], 'one_user.json')) as file:
            self.test_user = json.load(file)

    def test_open_register(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user1.username, "albert")
        self.assertEqual(self.user1.first_name, "Albert")

    # CREATE - Регистрация нового пользователя
    def test_create_user(self):
        response = self.client.post(reverse('register'), self.test_user, follow=True)
        self.assertEqual(response.status_code, 200)

    # LOGIN
    def test_read_user(self):
        response = self.client.post(reverse('user_login'),
                                    {'username': self.user1.username,
                                     'password': self.user1.password})
        self.assertEqual(response.status_code, 200)

    # UPDATE - обновление данных пользователя
    def test_update_user(self):
        # with no login
        response = self.client.get(self.update_pk_1)
        self.assertRedirects(response, self.login_url, 302, 200)
        self.assertEqual(response.status_code, 302)

        # with login
        self.client.force_login(self.user1)
        response = self.client.post(reverse('update_user', kwargs={'pk': self.user1.pk}),
                                    date=self.test_user)
        self.assertEqual(response.status_code, 200)

        # update other users
        self.client.force_login(self.user2)
        response = self.client.post(reverse_lazy('update_user', kwargs={'pk': self.user3.pk}),
                                    date=self.test_user)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

    # DELETE - удаления пользователя
    def test_user_delete_view(self):  #
        # with no login
        response = self.client.get(self.delete_pk_1)
        self.assertRedirects(response, self.login_url, 302, 200)
        self.assertEqual(response.status_code, 302)

        # with login
        self.client.force_login(self.user1)
        response = self.client.get(reverse('delete_user',
                                           kwargs={'pk': self.user1.pk}))
        self.assertEqual(response.status_code, 200)

        # delete other users
        response = self.client.get(reverse_lazy('delete_user', kwargs={'pk': 2}))
        self.assertRedirects(response, reverse_lazy('users'))
