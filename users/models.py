from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['-date_joined']
