from django.db import models

# Create your models here.
class movie_model(models.Model):
    rdate = models.DateField()
    mname = models.CharField(max_length=30)
    hero = models.CharField(max_length=30)
    heroine = models.CharField(max_length=30)
    rating = models.IntegerField()
