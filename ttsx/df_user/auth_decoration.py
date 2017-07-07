from django.shortcuts import render,redirect

def auth(func):
    def wrapper(request,*args,**kwargs):
        if request.session.has_key('uid'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/usr/login/')
    return wrapper