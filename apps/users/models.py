from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=255, unique=True)

    avatar = models.ImageField(
        upload_to='avatar',
        blank=True, null=True)
    gender = models.CharField(
        max_length=255,
        blank=True, null=True)
    is_student = models.BooleanField(
        default=False)
    is_teacher = models.BooleanField(
        default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('-id',)
