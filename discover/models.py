from django.db import models
from disease.models import Disease
from country.models import Country
# Create your models here.
class Discover(models.Model):
    class Meta:
        unique_together = (('cname', 'disease_code'),)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc_date = models.DateField()
