from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    percentage = models.FloatField()
