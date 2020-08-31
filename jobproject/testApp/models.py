from django.db import models

# Create your models here.
class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=64)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()