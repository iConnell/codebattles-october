from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=256)
    logo = models.ImageField()
    summary = models.CharField(max_length=256, blank=True, null=True)
    # advocates = models.

    def __str__(self):
        return self.name


class Advocate(models.Model):
    name = models.CharField(max_length=256)
    profile_pic = models.ImageField()
    short_bio = models.CharField(max_length=256, null=True, blank=True)
    long_bio = models.CharField(max_length=1024, null=True, blank=True)
    advocate_years_exp = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    youtube = models.CharField(max_length=256, null=True, blank=True)
    twitter = models.CharField(max_length=256, null=True, blank=True)
    github = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name
    