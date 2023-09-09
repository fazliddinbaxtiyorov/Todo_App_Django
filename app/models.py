from django.db import models


# Create your models here.


class TodoApp(models.Model):
    title = models.CharField(max_length=120)
    deadline = models.DateField()
    description = models.CharField(max_length=120)
