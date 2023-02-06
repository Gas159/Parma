import json
import os
from task_manager.settings import FIXTURE_DIRS
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from labels.models import Labels
from statuses.models import Status
from users.models import Users


class CrudStatusesTest(TestCase):
    fixtures = ['users.json', 'labels.json', 'tasks.json', 'statuses.json']

    def setUp(self):
        self.user = Users.objects.get(pk=1)
        self.label = Labels.objects.get(pk=1)
        self.login_url = reverse_lazy('user_login')
        self.home = reverse_lazy('home')
        self.update_pk_1 = reverse_lazy('update_status', kwargs={'pk': 1})
        self.delete_pk_1 = reverse_lazy('delete_status', kwargs={'pk': 1})
        self.update_pk_2 = reverse_lazy('update_status', kwargs={'pk': 2})
        self.Status = Status.objects.get(pk=1)
        with open(os.path.join(FIXTURE_DIRS[0], 'one_status.json')) as file:
            self.test_status = json.load(file)

    def test_access(self):
        '''Незалогинение пользователи получают редирект'''
        resp1 = self.client.get(reverse('create_status'))
        self.assertEqual(resp1.status_code, 302)
        resp2 = self.client.get(reverse('statuses'))
        self.assertEqual(resp2.status_code, 302)
        resp3 = self.client.get(reverse('update_status', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)
        resp4 = self.client.get(reverse('delete_status', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)

        '''Залогинимся'''
        self.client.force_login(self.user)
        resp1 = self.client.get(reverse('create_status'))
        self.assertEqual(resp1.status_code, 200)
        resp2 = self.client.get(reverse('statuses'))
        self.assertEqual(resp2.status_code, 200)
        resp3 = self.client.get(reverse('update_status', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 200)
        resp4 = self.client.get(reverse('delete_status', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 200)

    # CREATE - Создание нового статуса
    def test_CreateStatus(self):
        self.client.force_login(self.user)

        '''Добавим статус'''
        resp = self.client.post(reverse('create_status'), {'name': 'status4'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('statuses'))

        '''Проверяем добавлен ли новый статус'''
        resp = self.client.get(reverse('statuses'))
        self.assertTrue(len(resp.context['statuses']) == 4)

    # READ - список всех статусов
    def test_ListStatuses(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('statuses'))
        self.assertTrue(len(resp.context['statuses']) == 3)

    # UPDATE - обновление статуса
    def test_UpdateStatus(self):
        self.client.force_login(self.user)
        s1 = Status.objects.get(pk=1)
        resp = self.client.post(reverse('update_status', kwargs={'pk': 1}),
                                data=self.test_status)
        self.assertEqual(resp.status_code, 302)
        s1.refresh_from_db()
        self.assertEqual(s1.name, 'update status 1')

    # DELETE - удаление статуса
    def test_DeleteStatus(self):
        self.client.force_login(self.user)
        self.assertEqual(Status.objects.count(), 3)
        resp = self.client.post(
            reverse('delete_status', kwargs={'pk': 3})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.get(pk=1).name, 'status 1')
        self.assertEqual(Status.objects.get(pk=2).name, 'status 2')

    def test_cant_delete_status_with_task(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.delete_pk_1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(first=Status.objects.count(), second=3)
