from django.db import models

# Create your models here.
class employee_crud_fdv_model(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eadd = models.CharField(max_length=250)
