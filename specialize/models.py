from django.db import models
from users.models import Users
from diseasetype.models import DiseaseType
# Create your models here.
class Specialize(models.Model):
    class Meta:
        unique_together = (('specialize','email'),)
    specialize = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    email = models.ForeignKey(Users, on_delete=models.CASCADE)