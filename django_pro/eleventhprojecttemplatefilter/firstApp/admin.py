from django.contrib import admin
from firstApp.models import filter_model
# Register your models here.
class filter_admin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']
admin.site.register(filter_model,filter_admin)
