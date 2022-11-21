from django.db import models
from diseasetype.models import DiseaseType

# Create your models here.
class Disease(models.Model):
    diseaseCode = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=140)
    disease_id = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)