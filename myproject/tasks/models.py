from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

