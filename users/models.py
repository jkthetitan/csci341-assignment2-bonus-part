from django.db import models
from country.models import Country
# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=60, primary_key=True)
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)