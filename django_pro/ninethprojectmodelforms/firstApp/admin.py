from django.contrib import admin
from firstApp.models import movie_model
# Register your models here.
class movie_admin(admin.ModelAdmin):
    list_display = ["rdate","mname","hero","heroine","rating"]
admin.site.register(movie_model,movie_admin)
