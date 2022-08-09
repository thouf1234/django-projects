from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):#this will execute f we use Student.objects.all()
        return super().get_queryset().filter(esal__gte=15000)
class CustomManager1(models.Manager):
    def get_queryset(self):#this will execute f we use Student.objects.all()
        return super().get_queryset().order_by('ename')
class CustomManager2(models.Manager):
    def get_queryset(self):#this will execute f we use Student.objects.all()
        return super().get_queryset().filter(eno__lt=5000)
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eadd = models.CharField(max_length=250)
    objects=CustomManager()
class ProxyEmployee1(Employee):#no separate table will be created
    objects=CustomManager1()
    class Meta:
        proxy=True
class ProxyEmployee2(Employee):#no separate table will be created
    objects=CustomManager2()
    class Meta:
        proxy=True
