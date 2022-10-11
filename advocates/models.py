from django.db import models
from company.models import Company

# Create your models here.

class Advocate(models.Model):
    name = models.CharField(max_length=256)
    profile_pic = models.ImageField()
    short_bio = models.CharField(max_length=256, null=True, blank=True)
    long_bio = models.CharField(max_length=1024, null=True, blank=True)
    advocate_years_exp = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Links(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + 'link'

    