from django.test import TestCase
from users.models import Trial

class TrialTests(TestCase):
    """Тесты для модели Trial"""

    @classmethod
    def setUpTestData(cls):
        """Заносит данные в БД перед запуском тестов класса"""

        cls.trial = Trial.objects.create(
            email='test@gmail.com'
        )
        cls.email_field = cls.trial._meta.get_field('email')

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        real_verbose_name = getattr(self.email_field, 'verbose_name')
        expected_verbose_name = 'Электронная почта'

        self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_max_length(self):
        """Тест параметра max_length"""

        real_max_length = getattr(self.email_field, 'max_length')

        self.assertEqual(real_max_length, 256)

    def test_unique(self):
        """Тест параметра unique"""

        real_unique = getattr(self.email_field, 'unique')

        self.assertFalse(real_unique)

    def test_string_representation(self):
        """Тест строкового отображения"""

        self.assertEqual(str(self.trial), str(self.trial.email))

    def test_model_verbose_name(self):
        """Тест поля verbose_name модели Trial"""

        self.assertEqual(Trial._meta.verbose_name, 'Триал')

    def test_model_verbose_name_plural(self):
        """Тест поля verbose_name_plural модели Trial"""

        self.assertEqual(Trial._meta.verbose_name_plural, 'Триалы')