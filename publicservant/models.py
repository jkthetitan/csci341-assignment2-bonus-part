from django.db import models
from users.models import Users
# Create your models here.
class PublicServant(models.Model):
    email = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50)
