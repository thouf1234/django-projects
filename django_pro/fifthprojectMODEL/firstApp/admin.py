from django.contrib import admin
from firstApp.models import students
# Register your models here.
class studentTable(admin.ModelAdmin):
    list_display=['id','name', 'rollno', 'percentage']

admin.site.register(students,studentTable)
