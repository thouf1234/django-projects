from django.contrib import admin
from firstApp.models import chennai,hyderabad,delhi
# Register your models here.
class adminjobschennai(admin.ModelAdmin):
    list_display = ['date','company','role','eligibility','address','email','phone']
class adminjobshyderabad(admin.ModelAdmin):
    list_display = ['date','company','role','eligibility','address','email','phone']
class adminjobsdelhi(admin.ModelAdmin):
    list_display = ['date','company','role','eligibility','address','email','phone']
admin.site.register(chennai,adminjobschennai)
admin.site.register(hyderabad,adminjobshyderabad)
admin.site.register(delhi,adminjobsdelhi)
