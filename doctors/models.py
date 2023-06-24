from django.db import models


# Create your models here.
class Vets(models.Model):
    vet_name = models.CharField(max_length=20)
    vet_calendly = models.CharField(max_length=200)
    vet_description = models.CharField(max_length=100)
    vet_email = models.EmailField()

    def save(self, *args, **kwargs):
        self.vet_name = "Dr. " + self.vet_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.vet_name
