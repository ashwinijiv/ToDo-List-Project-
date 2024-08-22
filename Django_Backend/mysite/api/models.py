from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Yet to Start")

    def __str__(self):
        return self.name
