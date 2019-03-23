from django.db import models

# Create your models here.
class Dailytask(models.Model):
    date=models.DateField(blank=False)
    workingproject=models.TextField(blank=False)
    company=models.TextField(blank=False)
    workinghour=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stage=models.TextField( blank=False)