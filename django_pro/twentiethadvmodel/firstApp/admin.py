from django.contrib import admin
from firstApp.models import Student, Teacher
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','address','rollno','marks']
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','email','address','subject','salary']
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
