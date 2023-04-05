from django.db import models

# Create your models here.

class Note (models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=8000)

    def __str__(self):
        return self.title
    