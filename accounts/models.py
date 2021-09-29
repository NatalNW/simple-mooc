from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Username', max_length=30, unique=True)
    name = models.CharField('Name', max_length=150, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Is Staff?', blank=True, default=False)
    is_active = models.BooleanField('Is Active?', blank=True, default=True)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True
