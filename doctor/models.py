from django.db import models
from users.models import Users
# Create your models here.
class Doctor(models.Model):
    email = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    degree_type = models.CharField(max_length=20)
