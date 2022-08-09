from django.shortcuts import render
import datetime
# Create your views here.
def tempview(request):
    date = datetime.datetime.now()
    my_dict = {'date_msg':date}
    return render(request,'tempApp/wish.html', context = my_dict)
