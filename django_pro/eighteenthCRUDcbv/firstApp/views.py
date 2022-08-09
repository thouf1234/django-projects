from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from firstApp.models import book_crud_cbv_model
from django.urls import reverse_lazy
# Create your views here.
class book_list_view(ListView):
    model=book_crud_cbv_model
    #default template_name is 'book_crud_cdv_model_list.html'
    #default context_object_name is 'book_crud_cdv_model_list' OR 'object'
    #template_name='firstApp/books.html' #giving our own template file (custom) is also possible
    #context_object_name='list_of_books' #we can also give our own context object name (if you are not commenting this line then in template file you have to use 'for bk in list_of_books')
class book_detail_view(DetailView):
    model=book_crud_cbv_model
    #default template_name is 'book_crud_cdv_model_detail.html'
    #default context_object_name is 'book_crud_cdv_model' OR 'object'
class book_create_view(CreateView):
    model=book_crud_cbv_model
    fields='__all__'
    #fields=('title','author','pages','price')#both the filelds in line no 18 and 19 are valid
    #default template name for create (using forms): book_crud_cdv_model_form.html
class book_update_view(UpdateView):
    model=book_crud_cbv_model
    fields=('title','pages','price')#specify which fields are allowed to change
    #default template name for update (using forms): book_crud_cdv_model_form.html
class book_delete_view(DeleteView):
    model=book_crud_cbv_model
    success_url=reverse_lazy('list')#success url represents the target page which should be displayed after successfull deletion (reason for reverse lazy is that it will waite untill deletion completed)
    #default template_name for confirmation page before deletion is 'book_crud_cdv_model_confirm_delete.html'
    #default context_object_name is 'book_crud_cdv_model'
