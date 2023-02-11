import json
import os
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from labels.models import Labels
from task_manager.settings import FIXTURE_DIRS
from users.models import Users
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import get_messages


class CrudLabelsTest(TestCase):
    ''' Dont forget your doc string '''
    fixtures = ['users.json', 'labels.json', 'tasks.json', 'statuses.json']

    def setUp(self):
        self.user = Users.objects.get(pk=1)
        self.label = Labels.objects.get(pk=1)
        self.login_url = reverse_lazy('user_login')
        self.create_url = reverse_lazy('register')
        self.home = reverse_lazy('home')
        self.update_pk_1 = reverse_lazy('update_label', kwargs={'pk': 1})
        self.delete_pk_1 = reverse_lazy('delete_label', kwargs={'pk': 1})
        self.update_pk_2 = reverse_lazy('update_label', kwargs={'pk': 2})
        self.label = Labels.objects.get(pk=1)
        self.user1 = Users.objects.get(pk=1)
        self.user2 = Users.objects.get(pk=2)
        self.user3 = Users.objects.get(pk=3)
        with open(os.path.join(FIXTURE_DIRS[0], 'one_label.json')) as file:
            self.test_label = json.load(file)
        self.my_message = 'Вы не авторизованы! Пожалуйста, выполните вход.'

    # Проверка доступа незалогиненым пользователям
    def test_access(self):
        '''Незалогинение пользователи получают редирект'''
        resp1 = self.client.get(reverse('create_label'))
        self.assertEqual(resp1.status_code, 302)
        resp2 = self.client.get(reverse('labels'))
        self.assertEqual(resp2.status_code, 302)
        resp3 = self.client.get(reverse('update_label', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)
        resp4 = self.client.get(reverse('delete_label', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)
        '''Залогинимся'''
        self.client.force_login(self.user)
        resp1 = self.client.get(reverse('create_label'))
        self.assertEqual(resp1.status_code, 200)
        resp2 = self.client.get(reverse('labels'))
        self.assertEqual(resp2.status_code, 200)
        resp3 = self.client.get(reverse('update_label', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 200)
        resp4 = self.client.get(reverse('delete_label', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 200)

        messages = list(get_messages(resp1.wsgi_request))
        self.assertEqual(len(messages), 4)
        for m in range(len(messages)):
            self.assertEqual(_(str(messages[m])), self.my_message)

    # CREATE - Создание новой метки
    def test_create_label(self):
        self.client.force_login(self.user)
        '''Добавим статус'''
        resp = self.client.post(reverse('create_label'), self.test_label)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('labels'))
        '''Проверяем добавлен ли новый статус'''
        self.assertEqual(Labels.objects.first().name, self.test_label.get('name'))
        resp = self.client.get(reverse('labels'))
        self.assertTrue(len(resp.context['labels']) == 4)

    # READ - список всех статусов
    def test_list_label(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('labels'))
        self.assertTrue(len(resp.context['labels']) == 3)

    def test_update_labels(self):
        self.client.force_login(self.user1)
        self.assertNotEqual(self.label.name, self.test_label.get("name"))

        response = self.client.post(self.update_pk_1, self.test_label)
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, self.test_label.get('name'))

    # DELETE - удаление статуса
    def test_delete_status(self):
        self.client.force_login(self.user)
        self.assertEqual(Labels.objects.count(), 3)
        resp = self.client.post(
            reverse('delete_label', kwargs={'pk': 3})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Labels.objects.count(), 2)
        self.assertEqual(Labels.objects.get(pk=2).name, 'label2')
        self.assertEqual(Labels.objects.get(pk=1).name, 'label1')

    def test_cant_delete_label_with_task(self):
        self.client.force_login(self.user2)
        count_label = Labels.objects.count()
        self.client.post(reverse('delete_label', kwargs={'pk': 1}))
        self.assertEqual(Labels.objects.count(), count_label)
