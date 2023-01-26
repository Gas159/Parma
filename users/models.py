# from django.db import models
# from django.urls.py import reverse
# # Create your models here.


from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    def __str__(self):
        return self.username


