import json
import os
from task_manager.settings import FIXTURE_DIRS
from django.test import TestCase
from django.urls import reverse_lazy
from tasks.models import Task
from labels.models import Labels
from users.models import Users


class CrudTasksTest(TestCase):
    fixtures = ['users.json', 'labels.json', 'tasks.json', 'statuses.json']

    def setUp(self):
        self.user1 = Users.objects.get(pk=1)
        self.user3 = Users.objects.get(pk=3)
        self.label = Labels.objects.get(pk=1)
        self.login_url = reverse_lazy('user_login')
        self.create = reverse_lazy('create_task')
        self.task = reverse_lazy('task', kwargs={'pk': 1})
        self.tasks = reverse_lazy('tasks')
        self.update_pk_1 = reverse_lazy('update_task', kwargs={'pk': 1})
        self.delete_pk_1 = reverse_lazy('delete_task', kwargs={'pk': 1})
        self.delete_pk_2 = reverse_lazy('delete_task', kwargs={'pk': 2})
        self.update_pk_2 = reverse_lazy('update_task', kwargs={'pk': 2})
        self.task1 = Task.objects.get(pk=1)
        with open(os.path.join(FIXTURE_DIRS[0], 'one_task.json')) as file:
            self.test_task = json.load(file)

    def test_open_all_tasks_page(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.tasks)
        self.assertEqual(response.status_code, 200)

    def test_open_all_tasks_page_without_authorization(self):
        response = self.client.get(self.tasks)
        self.assertEqual(response.status_code, 302)

    def test_open_task_view_page(self):
        self.client.force_login(self.user1)
        resp3 = self.client.get(self.task)
        self.assertEqual(resp3.status_code, 200)

    def test_open_create_status_page_without_login(self):
        response = self.client.get(self.create)
        self.assertEqual(response.status_code, 302)

    def test_open_create_page_with_login(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.create)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.create,
                                    self.test_task)
        self.assertRedirects(response, self.tasks)
        self.assertEqual(response.status_code, 302)

        self.task3 = Task.objects.get(pk=3)
        self.assertEqual(self.task3.name,
                         self.test_task.get('name'))
        self.assertEqual(Task.objects.count(), 3)

    def test_open_update_tasks_page_without_login(self):
        response = self.client.get(self.update_pk_1)
        self.assertEqual(response.status_code, 302)

    def test_open_update_tasks_page_with_login(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.update_pk_1)
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        self.client.force_login(self.user1)
        self.task = Task.objects.get(pk=1)
        self.assertNotEqual(self.task.name,
                            self.test_task.get("name"))

        response = self.client.post(self.update_pk_1,
                                    data=self.test_task)
        self.assertEqual(response.status_code, 302)

        self.task = Task.objects.get(pk=1)
        self.assertEqual(self.task.name, self.test_task.get('name'))

    def test_open_delete_page_without_login(self):
        response = self.client.get(self.delete_pk_1)
        self.assertEqual(response.status_code, 302)

    def test_open_delete_page_with_login(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.delete_pk_1)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        self.client.force_login(self.user1)
        response = self.client.delete(self.delete_pk_1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        with self.assertRaises(expected_exception=Task.DoesNotExist):
            Task.objects.get(pk=1)

    def test_delete_task_if_user_is_not_author(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.delete_pk_2)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.tasks)
        self.assertEqual(Task.objects.count(), 2)
