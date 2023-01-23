from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from users.models import Users


# setUp – выполняется перед запуском каждого теста;
# tearDown – выполняется после завершения каждого теста;
# setUpTestData – выполняется перед запуском всех тестов конкретного класса.

# tes: # python manage.py 1test my_app.tests.test_models.TrialTests
# 		python manage.py 1test


# self.post = Users.objects.create(
#     title='A good title',
#     body='Nice body content',
#     author=self.user,
# )
# def test_string_representation(self):
#     post = Users(username='A sample title')
#     self.assertEqual(str(post), post.title)

# def test_get_absolute_url(self):  # new
#     self.assertEqual(self.post.get_absolute_url(), '/')
#
# def test_post_content(self):
#     self.assertEqual(f'{self.post.title}', 'A good title')
#     self.assertEqual(f'{self.post.author}', 'testuser')
#     self.assertEqual(f'{self.post.body}', 'Nice body content')
#
# def test_post_list_view(self):
#     response = self.client.get(reverse('home'))
#     self.assertEqual(response.status_code, 200)
#     self.assertContains(response, 'Nice body content')
#     self.assertTemplateUsed(response, 'home.html')
#
# def test_post_detail_view(self):
#     response = self.client.get('/post/1/')
#     no_response = self.client.get('/post/100000/')
#     self.assertEqual(response.status_code, 200)
#     self.assertEqual(no_response.status_code, 404)
#     self.assertContains(response, 'A good title')
#     self.assertTemplateUsed(response, 'post_detail.html')
# def test_SignUp(self):
#     resp = self.objects.get(reverse('register'))
#     self.assertEqual(resp.status_code, 200)

# def test_post_create_view(self):  # new
#     response = self.client.post(reverse('post_new'), {
#         'title': 'New title',
#         'body': 'New text',
#         'author': self.user,
#     })
#     self.assertEqual(response.status_code, 200)
#     self.assertContains(response, 'New title')
#     self.assertContains(response, 'New text')
#
# def test_post_update_view(self):  # новое
#     response = self.client.post(reverse('post_edit', args='1'), {
#         'title': 'Updated title',
#         'body': 'Updated text',
#     })
#     self.assertEqual(response.status_code, 302)


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
        # self.assertTemplateUsed(response, template_name='register.html')
        # self.assertRedirects(response, reverse('users'))

    def test_read_user(self):
        response = self.client.post(reverse('user_login'),
                                    {'username': 'ivan_ivanov',
                                     'password': 'qwerty'})
        # self.assertTrue(len(response.context['users']) == 1)

        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'home.html')
        # self.assertRedirects(response, reverse('home'))

    # UPDATE - обновленние данных пользователя
    def test_update_user(self):
        self.client.login(username='ivan_ivanov', password='qwerty')
        response = self.client.post(reverse('update_user',
                                            kwargs={'pk': self.user.pk}),
                                    {'first_name': 'Ivan',
                                     'last_name': 'Ivanov',
                                     'email': 'ivanivanov@gmail.com'})
        self.assertEqual(response.status_code, 302)
        # print(response.context)
        # self.assertEqual(User.objects.get(id=1).first_name, 'Ivan')
        # self.assertEqual(self.user.last_name, 'Ivanov')
        # self.assertEqual(self.user.email, 'ivanivanov@gmail.com')


    # DELETE - удаления пользователя
    def test_user_delete_view(self):  # новое
        response = self.client.post(
            reverse('delete_user', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
