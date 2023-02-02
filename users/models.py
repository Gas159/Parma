from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['-date_joined']
