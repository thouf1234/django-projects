from django.contrib import admin
from firstApp.models import Student, Teacher, ContactInfo
# Register your models here.
class StudentAdmin(admin.ModelAdmin):#adding student details in admin pannel will reflect in contact info table too(i.e. entering data from the child table of parent's field will reflect the data in parent's table too)
    list_display=['id','name','email','address','rollno','marks']
class TeacherAdmin(admin.ModelAdmin):#adding teacher details in admin pannel will reflect in contact info table too
    list_display=['id','name','email','address','subject','salary']
class ContactInfoAdmin(admin.ModelAdmin):
    list_display=['id','name','email','address']
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)
