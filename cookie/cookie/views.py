from django.shortcuts import render
from datetime import datetime, timedelta

# COOKIES 

# def setcookie(request):
#     a =render(request, 'setcookie.html')
#     a.set_cookie('name','saksham',expires=datetime.utcnow()+timedelta(days=2))
#     a.set_cookie('age','21',max_age=25)
#     a.set_cookie('location','alld')
#     a.set_cookie('trade','adit')
#     return a
    
    
# def getcookie(request):
#     b= request.COOKIES['name']
#     d= request.COOKIES['age']
#     e= request.COOKIES['location']
#     f= request.COOKIES['trade']
#     return render(request,'getcookie.html',{'name':b,'age':d,'location':e,'trade':f})
    
# def deletecookie(request):
#     a = render(request,'deletecookie.html')
#     a.delete_cookie('name')
#     return a



# SESSION
def setsession(request):
    request.session['name'] = 'Saksham'
    # request.session.set_expiry(20) #delete session name in 20seconds
    request.session['age'] = '21'
    request.session['nsti'] = 'alld'
    request.session['location'] = 'UP'
    return render(request,'setsession.html')

def getsession(request):
    a=request.session['name']
    b=request.session['age']
    c=request.session['nsti']
    d=request.session['location']
    keys = request.session.keys()
    values = request.session.values()
    return render(request,'getsession.html',{'name':a,'age':b,'nsti':c,'location':d,'keys':keys})

def deletesession(request):
    # del request.session['name']
    request.session.flush = ()
    return render(request,'deletesession.html')