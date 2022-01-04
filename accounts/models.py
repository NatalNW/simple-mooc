from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
import re

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Username', max_length=30, unique=True,
        validators=[validators.RegexValidator(
            re.compile('^[\w.@+--]+$'),
            'The username can only contain letters, digits or the following characters: @/./+/-/_',
            'invalid'
        )]
    )
    name = models.CharField('Name', max_length=150, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Is Staff?', blank=True, default=False)
    is_active = models.BooleanField('Is Active?', blank=True, default=True)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        #full_name = f'{self.first_name} {self.last_name}'
        return str(self)

    def get_short_name(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
