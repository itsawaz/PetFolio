from django.db import models
from django.contrib.auth.models import User

# Create your models here

class PetoManager(models.Manager):
    pass

class Peto(models.Model):
    username = models.CharField(max_length=20)
    pet_type = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    bio = models.CharField(max_length=1000)
    objects = PetoManager()

    def __str__(self):

        return self.username
