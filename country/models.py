from django.db import models

# Create your models here.
class Country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()

