from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import *
from .models import*
import schedule
import time

# Create your views here.
def SignUp(request):
    #return HttpResponse(request.method)
    myform=UserCreationForm(request.POST or None)
    data={"form":myform,"title":"User Registration"}
    if (request.method=="POST"):
        if myform.is_valid():
            user=myform.save()
            login(request,user)
            # messages.success(request,"welcome you are logged in")
            return redirect('/userapp/gotohomepage')
            
    return render(request,"registration/registration.html",data)
def TestjsonData(request):
    from django.http import JsonResponse
    # from rest_framework.parsers import JSONPARSER
    import json,urllib
    import schedule
    import time
    import urllib
    from urllib.request import urlopen
    import requests
    headers: {
       "Authorization": "Bearer=75d48d7f-39a8-472a-8e6a-d8375feb477a"
    }
    url="http://api.coincap.io/v2/assets?"
    x=requests.get(url)
    y=x.json()
    for d in y.keys():
        if d =='data':
            for f in y[d]:
                ddata={'dtx':y[d]}
            return render(request,'jsontest.html',ddata)
            return HttpResponse("json")
        schedule.every(4).seconds.do(TestjsonData)
        while True:
            schedule.run_pending()
def UserLogout(request):
    txt="you have logged out"
    data={"text":txt}
    return render(request,"registration/logout.html",data)
def UForm(request):
    df=UserForm()
    dt="please post your comment"
    bt="submit your comment"
    data={"df":df,"formtitle":dt,"buttontext":bt}
    return render(request,"blank_form.html",data)

def Gotohomepage(request):
    return render(request,"homepage.html")
def UserMessage(request):
    if request.method=="POST":
        u=userclass(request.POST)
        print(request.POST.get ("names"))
        print(request.POST.get ("email"))
        print(request.POST.get ("phone"))
        print(request.POST.get ("message"))
    u=userclass(initial={'names':"anny"})
    data={"forms":u}
    return render(request,"usermessage.html",data)
def SendMessage(request):
    # if request.method=="POST":
    #     u=Messageform(request.POST)
    #     if u.is_valid():
    #         u.save()
    u=Messageform()
    data={"forms":u}
    return render(request,"usermessage.html",data)

def msgFormx(request):
    df=msgForm()
    dt="send your message here"
    bt="send message"
    data={"df":df,"formtitle":dt,"buttontext":bt}
    return render(request,"blank_form.html",data)

def UserIndex(request):
    data={}
    return render(request,"crypto.html",data)


def Usertest(request):
    dollars=570
    amount=3000
    data={"dollars":dollars,"amount":amount,"total":dollars*amount}
    return render(request,"testing.html",data)



def HomePage(request) :
    return HttpResponse("<h2>welcome!</h2>")

def Custom(request,name):
    n=name
    print("welcome mr " ,n)
    return HttpResponse("<h2>welcome!</h2>")
def Activity(request,name,crypto,price)  :
    na=name
    c=crypto
    p=price
    print("dear", na,"the price of" ,  c,"is",price,"usd" )
    return HttpResponse("<h2> Dear "+na+" <br> the price of "+c+" <br> is "+str(p)+"  </h2>")
def UserFeedback(request):
    if request.method=="POST":
        form=UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Code Band'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect("/userapp/userapp/userfeedbackviews")
    form= UserFeedbackForm()
    data={"form":form}
    return render(request,"usermessage.html",data)

def UserFeedBackView(request):
    allfeedbacks=Userfeedback.objects.all()
    data={"allusers":allfeedbacks}
    return render(request,"userfeedback.html",data)
def UsermailView(request):
    allfeedbacks=Sendmailmsg.objects.all()
    data={"allusers":allfeedbacks}
    return render(request,"mailview.html",data)
def Emailsender(request):
    from django.http import JsonResponse
    # from rest_framework.parsers import JSONPARSER
    import json,urllib
    import urllib
    from urllib.request import urlopen
    import requests
    import schedule
    import time

    headers: {
       "Authorization": "Bearer=75d48d7f-39a8-472a-8e6a-d8375feb477a"
    }
    if request.method=="POST":
        form=UserEmailform(request.POST)
        if form.is_valid():
            form.save()
            url="http://api.coincap.io/v2/assets?"
        x=requests.get(url)
        y=x.json()
        for d in y.keys():
            if d == 'data':      
                mailname=form.cleaned_data.get('names').title()
                print(mailname)
                for f in y[d]:
                        rslt=f.get('name')
                        if rslt==mailname:
                            msg=f.get('changePercent24Hr')
                            subject= 'Crypto tracker'
                            message= " The 24hrs% change of " + rslt +" is " + msg
                            recipient=form.cleaned_data.get('email')
                            send_mail(subject,
                            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                            messages.success(request, 'Success!')
                            return redirect("/userapp/jsonres")
    form= UserEmailform()
    data={"form":form}
    return render(request,"usermessage.html",data)
