from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email является обязательным полем')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество (при наличии)')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')

    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        indexes = [
            models.Index(fields=['email']),
        ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'


class Manager(User):
    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(Manager, self).save(*args, **kwargs)


class Guest(User):
    is_blocked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
