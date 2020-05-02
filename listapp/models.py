from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.title