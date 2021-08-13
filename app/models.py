from django.db import models
from django.contrib.auth.models import User


class LogInfo(models.Model):
    login = models.CharField(max_length=255, default='login')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    workspace_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname} {self.date} {self.workspace_number}"