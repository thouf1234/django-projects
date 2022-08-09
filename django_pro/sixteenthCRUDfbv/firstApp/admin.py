from django.contrib import admin
from firstApp.models import employee_crud_fdv_model
# Register your models here.
class employee_crud_fdv_admin(admin.ModelAdmin):
    list_display=['id','eno', 'ename', 'esal','eadd']

admin.site.register(employee_crud_fdv_model,employee_crud_fdv_admin)
