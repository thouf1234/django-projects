from django.db import models

# Create your models here.
class chennai(models.Model):
    date = models.DateField()
    company = models.CharField(max_length= 100)
    role = models.CharField(max_length= 100)
    eligibility = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length= 100)
class hyderabad(models.Model):
    date = models.DateField()
    company = models.CharField(max_length= 100)
    role = models.CharField(max_length= 100)
    eligibility = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length= 100)
class delhi(models.Model):
    date = models.DateField()
    company = models.CharField(max_length= 100)
    role = models.CharField(max_length= 100)
    eligibility = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length= 100)
