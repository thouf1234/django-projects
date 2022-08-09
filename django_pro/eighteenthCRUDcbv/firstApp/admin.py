from django.contrib import admin
from firstApp.models import book_crud_cbv_model
# Register your models here.
class book_crud_cbv_admin(admin.ModelAdmin):
    list_display = ['title','author','pages','price']
admin.site.register(book_crud_cbv_model,book_crud_cbv_admin)
