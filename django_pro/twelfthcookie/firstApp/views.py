from django.shortcuts import render

# Create your views here.
def temp_cookie_view(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES.get('count',0))
        new_count=count+1
    else:
        new_count=1
    response=render(request,'firstApp/temp_cookie.html',{'count':new_count})
    response.set_cookie('count',new_count)
    return response
def perm_cookie_view(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES.get('count',0))
        new_count=count+1
    else:
        new_count=1
    response=render(request,'firstApp/temp_cookie.html',{'count':new_count})
    response.set_cookie('count',new_count,max_age=10)
    return response
def name_view(request):
    return render(request,'firstApp/name.html')
def age_view(request):
    name=request.GET['name']
    response=render(request,'firstApp/age.html')
    response.set_cookie('name',name)
    return response
def gf_view(request):
    age=request.GET['age']
    response=render(request,'firstApp/gf.html')
    response.set_cookie('age',age)
    return response
def result_view(request):
    gf=request.GET['gf']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    response=render(request,'firstApp/result.html',{'name':name,'age':age,'gf':gf})
    return response
