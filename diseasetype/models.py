from django.db import models

# Create your models here.


class DiseaseType(models.Model):
    dt_id = models.IntegerField(primary_key = True)
    description = models.CharField(max_length=140)