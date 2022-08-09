from django.contrib import admin
from firstApp.models import Employee,ProxyEmployee1,ProxyEmployee2
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eadd']
class ProxyEmployee1Admin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eadd']
class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eadd']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee1,ProxyEmployee1Admin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)
