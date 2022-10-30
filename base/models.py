from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=256)
    logo = models.ImageField()
    summary = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class Advocate(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    profile_pic = models.ImageField()
    bio = models.CharField(max_length=256, default='')
    twitter = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name
    