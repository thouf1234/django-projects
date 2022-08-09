from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):#this will execute if we use Student.objects.all()
        return super().get_queryset().order_by('eno')
    def get_emp_sal_range(self,esal1,esal2):
        return super().get_queryset().filter(esal__range=(esal1,esal2))
    def get_emp_sorted_by(self,param):
        return super().get_queryset().order_by(param)
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eadd = models.CharField(max_length=250)
    objects=CustomManager()
