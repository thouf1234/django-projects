from django.db import models
from django.urls import reverse
# Create your models here.
class book_crud_cbv_model(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    pages = models.PositiveIntegerField()
    price = models.FloatField()
    def get_absolute_url(self):#for both create and update by default django use same form so on submitting that form which page has to be displayed is said by this method
        #return reverse('list')#to display '/index/retrievelist' after clicking the submit button of the form in the template(book_crud_cbv_model_form) of view class(book_create_view) having parent 'CreateView'
        return reverse('detail',kwargs={'pk':self.pk})#to display '/index/retrivedetail/(?P<pk>\d+)/$' after clicking the submit button of the form in the template(book_crud_cbv_model_form) of view class(book_create_view) having parent 'CreateView'
        #for every entry in the database pk(primary key) will internally be maintained by the django
