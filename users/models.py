# from django.contrib.auth.models import AbstractUser
#
#
# class Users(AbstractUser):
#     def __str__(self):
#         return self.get_full_name()
#
#     class Meta:
#         ordering = ['-date_joined']

"""Declare models for YOUR_APP app."""
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from workplaces.models import Workplace


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        # user.password = make_password(password)
        # print(password)
        # user.password = '123123'
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and     password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff True")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser True")
        return self._create_user(email, password, **kwargs)


class Users(AbstractUser):
    username = None
    # first_name = None
    # last_name = None
    email = models.CharField(_('email address'), max_length=123, blank=False, null=False,
                             unique=True, help_text='email may be wrong')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    full_name = models.CharField(_('full name'), max_length=1000, null=True, blank=True)
    user_id = models.CharField(_('session id'), max_length=10000, null=True, blank=True)
    verification_code_time = models.IntegerField(_('time left for session id'),
                                                 null=True, blank=True)
    verification_code = models.IntegerField(_('verification code'), null=True, blank=True)
    workplace = models.ForeignKey(Workplace, on_delete=models.SET_NULL,
                                  verbose_name=_('workplace'), null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return self.last_name + " " + self.first_name

    class Meta:
        ordering = ['-date_joined']

    #     class Meta:
    # #         ordering = ['-date_joined']
    #
