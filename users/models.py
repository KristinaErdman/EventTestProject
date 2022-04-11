from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email является обязательным полем')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(password=password)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Type(models.TextChoices):
        MANAGER = 'manager', 'Менеджер'
        GUEST = 'guest', 'Гость'

    type = models.CharField(max_length=7, choices=Type.choices, blank=False, default=Type.GUEST,
                            verbose_name='Тип пользователя')
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

    def save(self, *args, **kwargs):
        password = kwargs.pop('password', None)
        if self.type == self.Type.MANAGER:
            self.is_staff = True
        if self.pk:
            previous = self.__class__.objects.get(pk=self.pk)
            if getattr(previous, 'password') != getattr(self, 'password'):
                self.set_password(self.password)
            self.type = previous.type
        else:
            if password:
                self.password = password
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
