from django.contrib import admin
from firstApp.models import employee_model, manager_model
# Register your models here.
class employee_admin(admin.ModelAdmin):
    list_display=['id','eno', 'ename', 'esal','eadd']

admin.site.register(employee_model,employee_admin)
admin.site.register(manager_model,employee_admin)
