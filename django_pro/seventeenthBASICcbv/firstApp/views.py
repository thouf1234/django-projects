from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.
#to return simple html response
class HelloworldView(View):
    def get(self,request):
        return HttpResponse('<h1>hellow world<h1>')
        #to return template response
class HelloworldTemplateView(TemplateView):
    template_name = 'firstApp/home.html'
#to return template response with context
class HelloworldTemplateContext(TemplateView):
    template_name = 'firstApp/info.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)#to get context object
        context['name']='B.MOHAMED THOUFEEQ'
        context['subject']='PYTHON'
        context['marks'] = 100
        print(context)
        return context
