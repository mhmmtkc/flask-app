from subprocess import CompletedProcess
from urllib import request
from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50, verbose_name="başlık")
    completed = models.BooleanField(verbose_name="durum")

    def __str__(self):
        return self.title
