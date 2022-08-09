from django.db import models

# Create your models here.
class filter_model(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    date=models.DateField()
