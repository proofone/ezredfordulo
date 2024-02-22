from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class Meta:
        verbose_name = "Felhasználó"

    username = models.EmailField("E-mail cím", unique=True)
    