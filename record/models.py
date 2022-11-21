from django.db import models
from users.models import Users
from country.models import Country
from disease.models import Disease
class Record(models.Model):
    class Meta:
        unique_together = (('email', 'cname', 'disease_code'),)
    email = models.ForeignKey(Users, on_delete=models.CASCADE)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()