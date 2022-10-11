from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=256)
    logo = models.ImageField()
    summary = models.CharField(max_length=256, blank=True, null=True)
    # advocates = models.

    def __str__(self):
        return self.name