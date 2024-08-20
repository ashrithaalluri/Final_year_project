from django.http import HttpResponse
from django.shortcuts import render,redirect
from appoinmentsystem.models import *
from django.contrib import messages


     

def mhome(request):
     return render (request,"mhome/index.html")

def register(request):
    if request.method=="POST":
        pname=request.POST.get("pname")
        cont=request.POST.get("cont")
        emai=request.POST.get("emai")
        addr=request.POST.get("addr")
        photo=request.FILES.get("photo")
        passw=request.POST.get("passw")
        p=patient_details()
        p.patient_name=pname
        p.patient_contact=cont
        p.patient_email=emai
        p.patient_address=addr
        p.patient_photo=photo
        p.pswrd=passw
        p.save()
    return render (request,"register.html")
    

def login(request):
    if request.method=='POST':
        usname=request.POST.get('username')
        passd=request.POST.get('pass')
        #user=authenticate(request,username=usname,password=passd)
        user=patient_details.objects.filter(patient_name=usname,pswrd=passd).count()
        if user > 0:
            #login (request,user)
            user=patient_details.objects.filter(patient_name=usname,pswrd=passd).first()
            request.session['usersession']=True
            request.session['userid']=usname
            request.session['u_id']=user.id
            return redirect("/apment/userhome/")
        else:
            return HttpResponse('Invalid Username And Password!!! ')   
    return render(request,"login.html")


def changepin(request):  
     return render(request,"adminhome/changepin.html")

def changepin_chk(request):   
     if request.method=="POST":
        uid=request.session['userid']
        op=request.POST.get("op")
        np=request.POST.get("np")
        cp=request.POST.get("cp")
        if patient_details.objects.filter(pswrd=uid,pswd=op) and np==cp: 
          u=patient_details.objects.get(pswrd=uid)
          print(op)
          print(np)
          print(cp)
          print(uid)
          u.pswrd=np
          u.save()
          messages.success(request,"password changed sucessfully...")     
        else:
          messages.success(request,"Unmatched old password...")     
     return render(request,"adminhome/changepin.html")



def LogoutPage(request):
    del request.session['usersession']
    return redirect('/')

def Dlogin(request):
    if request.method=='POST':
        Dsname=request.POST.get('username')
        passd=request.POST.get('pass')
        #user=authenticate(request,username=usname,password=passd)
        user=doctor_details.objects.filter(dr_name=Dsname,dr_contact=passd).count()
        if user > 0:
            #login (request,user)
            user=doctor_details.objects.filter(dr_name=Dsname,dr_contact=passd).first()
            request.session['drsession']=True
            request.session['drid']=Dsname
            request.session['d_id']=user.id
            return redirect("/apment/adminhome/")
        else:
            return HttpResponse('Invalid Username And Password!!! ')   
    return render(request,"Dlogin.html")

def DLogoutPage(request):
    del request.session['drsession']
    return redirect('/')
