from django.contrib import admin
from firstApp.models import employee
# Register your models here.
class emplo(admin.ModelAdmin):
    list_display= ['eno','ename','esal','eaddr']
admin.site.register(employee,emplo)
