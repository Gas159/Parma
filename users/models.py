# from django.db import models
# from django.urls import reverse
# # Create your models here.


from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    def __str__(self):
        return self.username

# class Users(models.Model):
#     username= models.CharField(max_length=255, verbose_name='Никнейм')
#     last_name= models.CharField(max_length=255, verbose_name='Фамилия')
#     first_name = models.CharField(max_length=255, verbose_name='Имя')
#     # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
#     # content = models.TextField(blank=True, verbose_name='Текст статьи')  # can empty null=True
#     # photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Фото', blank=True)
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     # time_update = models.DateTimeField(auto_now=True)
#     # cat = models.ForeignKey('Category', on_delete=models.PROTECT,
#     #                         verbose_name='Категория')  # related_name='get_posts' instead women_set
#     # is_published = models.BooleanField(default=True)
#
#     class Meta:  # class for admin panel
#         verbose_name = 'Пользователи'
#         verbose_name_plural = 'Пользователи'
#         # ordering = ['-time_create', 'title']
#         ordering = ['time_create', 'name']  # Указывать для пагинации (UnorderedObjectListWarning:)
#
#     # def get_absolute_url(self):
#     #     return reverse('post', kwargs={'post_slug': self.slug})
#
#     def __str__(self):
#         return f'{self.name} id:{self.id}'


from django.db import models

class Trial(models.Model):
    """Простая модель пользовательского триала"""

    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=256,
        unique=False,
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Триал'
        verbose_name_plural = 'Триалы'