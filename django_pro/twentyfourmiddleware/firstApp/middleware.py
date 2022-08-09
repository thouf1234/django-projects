class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):#this __call__ will execute when the request approaches the middleware
        print("this line printed as a part of pre-processiong of request")#process inside middleware after getting the request from the user or other middleware and before forwarding the request to the view function
        response=self.get_response(request)#this will forward response to the next level (either django view function(if there is no middleware after this middleware in the MIDDLEWARE list inside settings.py ) or next middleware(if there is middleware after this middleware in the MIDDLEWARE list inside settings.py) in middleware chain) (i.e. sending the request and getting responce)
        print("this line printed as a part of post-processiong of request")#process inside middleware after getting the responce from the view function and before forwarding the responce to the end user
        return response#middleware return the processed response to the end user
from django.http import HttpResponse
class AppMaintananceMiddleware(object):
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):#this __call__ will execute when the request approaches the middleware(ie.e when the middleware is called for processing the request)
        return HttpResponse("Currently Application Is Under Maintanance...Please Try After 2 Days!!!")#process inside middleware after getting the request from the user or other middleware and before forwarding the request to the view function
        #here as the application is under maintanance we dont need to forward the request either to another middleware or the django view function and so we skipp them and just return the responce with maintanance information
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):
        response=self.get_response(request)#just get the request
        return response#just return the response
    def process_exception(self,request,exception):#logic here will be execute if an exception/error occur in the view
        s1="<h1>Currently We Are Facing Technical Problems...Please Try After Some Time</h1>"
        s2="<h1>Raised Exception:{}</h1>".format(exception.__class__.__name__)
        s3="<h1>Raised Exception Message:{}</h1>".format(exception)
        return HttpResponse(s1+s2+s3)
class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):#this __call__ will execute when the request approaches the middleware
        print("this line printed by FirstMiddleware as a part of pre-processiong of request")#process inside middleware after getting the request from the user or other middleware and before forwarding the request to the view function
        response=self.get_response(request)#this will forward response to the next level (either django view function(if there is no middleware after this middleware in the MIDDLEWARE list inside settings.py ) or next middleware(if there is middleware after this middleware in the MIDDLEWARE list inside settings.py) in middleware chain) (i.e. sending the request and getting responce)
        print("this line printed by FirstMiddleware as a part of post-processiong of request")#process inside middleware after getting the responce from the view function and before forwarding the responce to the end user
        return response#middleware return the processed response to the end user
class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):#this __call__ will execute when the request approaches the middleware
        print("this line printed by SecondMiddleware as a part of pre-processiong of request")#process inside middleware after getting the request from the user or other middleware and before forwarding the request to the view function
        response=self.get_response(request)#this will forward response to the next level (either django view function(if there is no middleware after this middleware in the MIDDLEWARE list inside settings.py ) or next middleware(if there is middleware after this middleware in the MIDDLEWARE list inside settings.py) in middleware chain) (i.e. sending the request and getting responce)
        print("this line printed by SecondMiddleware as a part of post-processiong of request")#process inside middleware after getting the responce from the view function and before forwarding the responce to the end user
        return response#middleware return the processed response to the end user
class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response= get_response
    def __call__(self,request):#this __call__ will execute when the request approaches the middleware
        print("this line printed by ThirdMiddleware as a part of pre-processiong of request")#process inside middleware after getting the request from the user or other middleware and before forwarding the request to the view function
        response=self.get_response(request)#this will forward response to the next level (either django view function(if there is no middleware after this middleware in the MIDDLEWARE list inside settings.py ) or next middleware(if there is middleware after this middleware in the MIDDLEWARE list inside settings.py) in middleware chain) (i.e. sending the request and getting responce)
        print("this line printed by ThirdMiddleware as a part of post-processiong of request")#process inside middleware after getting the responce from the view function and before forwarding the responce to the end user
        return response#middleware return the processed response to the end user
