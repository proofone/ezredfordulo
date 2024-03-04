from django.db import models
from django.contrib.auth.models import AbstractUser


kiiras_status_choices = (('draft', "Vázlat"), ('public', "Publikus"), ('canceled', "Visszavont"))


class User(AbstractUser):
    class Meta:
        verbose_name = "Felhasználó"
        verbose_name_plural = "Felhasználók"

    username = models.EmailField("E-mail cím", unique=True)
    

class Kiiras(models.Model):
    class Meta:
        verbose_name = "Pályázati kiírás"
        verbose_name_plural = "Pályázati kiírások"

    title = models.CharField("Cím", max_length=100)
    description = models.TextField("Tartalom", blank=True)
    status = models.TextField(choices=kiiras_status_choices)
    pub_date = models.DateTimeField("Publikáció ideje", blank=True, null=True)
    deadline = models.DateTimeField("Beadási határidő", blank=True, null=True)
    