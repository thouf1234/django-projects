from django.shortcuts import render
from firstApp import forms
# Create your views here.
def form_view(request):
    if request.method=='POST':
        form=forms.djforms(request.POST)
        name=request.POST['name']
        if form.is_valid():
            quantity=form.cleaned_data['quantity']
            request.session[name]=quantity
            request.session.set_expiry(180)
    form=forms.djforms()#we are using form=forms.djforms() to display the fresh empty form after submitting it. if we dont give this, {'form':form} in libe number 16 will consider the form of line no 6 as it will then display the form with previously entered data on veery click on submit form
    return render(request,'firstApp/form.html',{'form':form})
def result_view(request):
    return render(request,'firstApp/view.html')

def del_view(request):
    for key in list(request.session.keys()):
        del request.session[key]
        request.session.modified=True
    return render(request,'firstApp/del.html')
