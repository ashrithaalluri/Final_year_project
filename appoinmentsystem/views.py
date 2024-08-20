from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.utils import timezone
import datetime
# Create your views here.
def adminhome(request):
    return render(request,"adminhome/home.html")
def video_conference(request):
     return render(request,"adminhome/video_conference.html")

def userhome(request):
    if 'q' in request.GET:
        q = request.GET['q']
        
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(dr_name__icontains=q)  )
        
        data= doctor_details.objects.filter(multiple_q)
        
    else:
        data = doctor_details.objects.all()
        
    context = {
        'data': data
    }
     #vehl=vehical_location.objects.all()
     
    return render(request,"adminhome/userhome.html",context)

def specializationform(request):
    if request.method=="POST":
        sname=request.POST.get("sname")
        sdes=request.POST.get("sdes")
        s=specialization_details()
        s.sp_name=sname
        s.sp_discription=sdes
        s.save()
        return redirect("/apment/specializationview/")
    return render(request,"adminhome/specializationform.html")

def specializationview(request,):
    spcl=specialization_details.objects.all()
    return render(request,"adminhome/specializationview.html",{'spcttl':spcl})

def specializationdelete(request,sp_id):
    spcl=specialization_details.objects.get(id=sp_id)
    spcl.delete()
    return redirect("/apment/specializationview/")

def specializationedit(request,sp_id):
    spcl=specialization_details.objects.get(id=sp_id)
    return render(request,"adminhome/specializationedit.html",{'spcttl':spcl})   

def specializationupdate(request,sp_id): 
    if request.method=="POST":
        sname=request.POST.get("sname")
        sdes=request.POST.get("sdes")
        s=specialization_details(id=sp_id)
        s.sp_name=sname
        s.sp_discription=sdes
        s.save()
    return redirect("/apment/specializationview/")   

def doctordetailsform(request):
    if request.method=="POST":
        dname=request.POST.get("dname")
        cont=request.POST.get("cont")
        emai=request.POST.get("emai")
        addr=request.POST.get("addr")
        drspec=request.POST.get("drspec")
        fdrspec=specialization_details.objects.get(id=drspec)
        photo=request.POST.get("photo")
        doctqual=request.POST.get("doctqual")
        exp=request.POST.get("exp")
        d=doctor_details()
        d.dr_name=dname
        d.dr_contact=cont
        d.dr_emailid=emai
        d.dr_address=addr
        d.dr_specialization=fdrspec
        d.dr_photo=photo
        d.dr_qualification=doctqual
        d.dr_experince=exp
        d.save()
        return redirect("/apment/doctordetailsview/")
    return render(request,"adminhome/doctordetailsform.html",{'spcl':specialization_details.objects.all})
    
def doctordetailsview(request):
    doct=doctor_details.objects.all()
    return render(request,"adminhome/doctordetailsview.html",{'doct':doct})

def doctordetailsdelete(request,d_id):
    doc=doctor_details.objects.get(id=d_id)
    doc.delete()
    return redirect("/apment/doctordetailsview/")

def doctordetailsedit(request):
    d_id=request.session['d_id']
    doc=doctor_details.objects.get(id=d_id)
    return render(request,"adminhome/doctordetailsedit.html",{'doc':doc,'spcl':specialization_details.objects.all})

def doctordetailsupdate(request,d_id):
    if request.method=="POST":
        dname=request.POST.get("dname")
        cont=request.POST.get("cont")
        emai=request.POST.get("emai")
        addr=request.POST.get("addr")
        drspec=request.POST.get("drspec")
        fdrspec=specialization_details.objects.get(id=drspec)
        photo=request.POST.get("photo")
        doctqual=request.POST.get("doctqual")
        exp=request.POST.get("exp")
        d=doctor_details(id=d_id)
        d.dr_name=dname
        d.dr_contact=cont
        d.dr_emailid=emai
        d.dr_address=addr
        d.dr_specialization=fdrspec
        d.dr_photo=photo
        d.dr_qualification=doctqual
        d.dr_experince=exp
        d.save()
    return redirect("/apment/doctordetailsview/")

def appoinmentscheduelform(request):
    if request.method=="POST":
        did=request.POST.get("did")
        fdid=doctor_details.objects.get(id=did)
        appoinday=request.POST.get("appoinday")
        appointime=request.POST.get("appointime")
        status=request.POST.get("status")
       
        a=appoinmentscheduel()
        a.doctor_id=fdid
        a.appoinment_day=appoinday
        a.hours_minutes=appointime
        a.appoinment_status=status
        
        a.save()
        return redirect("/apment/appoinmentscheduelview/")

    return render(request,"adminhome/appoinmentscheduelform.html",{'doct':doctor_details.objects.all,'pati':patient_details.objects.all})

def bookappoinment(request,sid):
        #sid=request.GET.get("id")
        did=request.GET.get("dr_id")
        pid=request.GET.get("pid")
        ad=request.GET.get("ad")
        hrms=request.GET.get("hrms")
        st=request.GET.get("st")

        fdid=doctor_details.objects.get(id=did)
        ptid=patient_details.objects.get(id=pid)
        #apt=appoinmentscheduel.objects.get(id=sid)
       
        a=appointement_req()
        a.doctor_id=fdid
        a.appoinment_day=ad
        a.hours_minutes=hrms
        a.appoinment_status='Booked'
        a.patient_id=ptid
        
        a.save()
        b=appoinmentscheduel.objects.get(id=sid)
        b.appoinment_status='Booked'
        b.save()
        return redirect("/apment/appoinmentstatusview/")


def appoinmentstatusview(request):
    u_id=request.session['u_id']
    appoi=appointement_req.objects.filter(patient_id=u_id)
    return render(request,"adminhome/appoinmentstatusview.html",{'appoi':appoi})

def appoinmentscheduelview(request):
    d_id=request.session['d_id']
    appoi=appoinmentscheduel.objects.filter(doctor_id=d_id)
    return render(request,"adminhome/appoinmentscheduelview.html",{'appoi':appoi})
def userappoinmentscheduelview(request):
    #d_id=request.session['d_id']
    if request.method == 'POST':
     appoinday=request.POST.get('appoinday')
     d_id=request.POST.get('did')
     appoi=appoinmentscheduel.objects.filter(doctor_id=d_id,appoinment_day=appoinday)
    return render(request,"adminhome/userappoinmentscheduelview.html",{'appoi':appoi})
def appoinmentschedueldelete(request,d_id):
    spcl=appoinmentscheduel.objects.get(id=d_id)
    spcl.delete()
    return redirect("/apment/appoinmentscheduelview/")

def appoinmentschedueledit(request,d_id):
    spcl=appoinmentscheduel.objects.get(id=d_id)
    return render(request,"adminhome/appoinmentschedueledit.html",{'spcl':spcl,'doct':doctor_details.objects.all,'pati':patient_details.objects.all})    

def userappoinmentschedueledit(request,d_id):
    spcl=appoinmentscheduel.objects.get(id=d_id)
    current_date = timezone.now().date()
    #current_day = current_date.day
    return render(request,"adminhome/userappoinmentschedueledit.html",{'cd':current_date,'spcl':spcl,'doct':doctor_details.objects.all,'pati':patient_details.objects.all})    

def appoinmentscheduelupdate(request,d_id):
     if request.method=="POST":
        did=request.POST.get("did")
        fdid=doctor_details.objects.get(id=did)
        appoin=request.POST.get("appoin")
        appoinday=request.POST.get("appoinday")
        status=request.POST.get("status")
        drspec=request.POST.get("drspec")
        pid=request.POST.get("pid")
        fpid=patient_details.objects.get(id=pid)
        a=appoinmentscheduel(id=d_id)
        a.doctor_id=fdid
        a.appoinment_date=appoin
        a.appoinment_day=appoinday
        a.appoinment_status=status
        a.patient_id=fpid
        a.save()
     return redirect("/apment/appoinmentscheduelview/")

def patientdetailsform(request):
    if request.method=="POST":
        pname=request.POST.get("pname")
        cont=request.POST.get("cont")
        emai=request.POST.get("emai")
        addr=request.POST.get("addr")
        photo=request.POST.get("photo")
        passw=request.POST.get("passw")
        p=patient_details()
        p.patient_name=pname
        p.patient_contact=cont
        p.patient_email=emai
        p.patient_address=addr
        p.patient_photo=photo
        p.pswrd=passw
        p.save()
        return redirect("/apment/patientdetailsview/")

    return render(request,"adminhome/patientdetailsform.html") 

def patientdetailsview(request):
    pati=patient_details.objects.all()
    return render(request,"adminhome/patientdetailsview.html",{'pati':pati})

def userpatientreportview(request):
    d_id=request.session['u_id']
    pati=patient_reports.objects.filter(patient_id=d_id)
    return render(request,"adminhome/userpatientreportview.html",{'pati':pati})

def patientdetailsdelete(request,p_id):
    pati=patient_details.objects.get(id=p_id)
    pati.delete()
    return redirect("/apment/patientdetailsview/")

def patientdetailsedit(request):
    d_id=request.session['u_id']
    #appoi=appoinmentscheduel.objects.filter(doctor_id=d_id)
    pati=patient_details.objects.get(id=d_id)
    return render(request,"adminhome/patientdetailsedit.html",{'pati':pati})

def patientdetailsupdate(request,p_id):
    if request.method=="POST":
        pname=request.POST.get("pname")
        cont=request.POST.get("cont")
        emai=request.POST.get("emai")
        addr=request.POST.get("addr")
        photo=request.POST.get("photo")
        passw=request.POST.get("passw")
        p=patient_details(id=p_id)
        p.patient_name=pname
        p.patient_contact=cont
        p.patient_email=emai
        p.patient_address=addr
        p.patient_photo=photo
        p.pswrd=passw
        p.save()
    return redirect("/apment/patientdetailsview/")



def patientreportform(request):
    if request.method=="POST" :
        pid=request.POST.get("pid")
        fpid=patient_details.objects.get(id=pid)
        patient=request.POST.get("patient")
        report=request.POST.get("report")
        pati=request.POST.get("pati")
        reffer=request.POST.get("reffer")
        freffer=doctor_details.objects.get(id=reffer)
        pr=patient_reports()
        pr.patient_id=fpid
        pr.patient_report_name=patient
        pr.report_file=report
        pr.report_date=pati
        pr.refferd_by=freffer
        pr.save()
        return redirect("/apment/patientreportview/")      
    return render(request,"adminhome/patientreportform.html",{'pid': patient_details.objects.all,'reff': doctor_details.objects.all})

def  patientreportview(request):
    report=patient_reports.objects.all()
    return render(request,"adminhome/patientreportview.html",{'report':report})  

def patientreportdelete(request,ref_id):
    report=patient_reports.objects.get(id=ref_id)
    report.delete()
    return redirect("/apment/patientreportview/")      

def patientreportedit(request,ref_id):
    report=patient_reports.objects.get(id=ref_id)
    return render(request,"adminhome/patientreportedit.html",{'report':report,'pid': patient_details.objects.all,'reff': doctor_details.objects.all})

def patientreportupdate(request,ref_id):
    if request.method=="POST" :
        pid=request.POST.get("pid")
        fpid=patient_details.objects.get(id=pid)
        patient=request.POST.get("patient")
        report=request.POST.get("report")
        pati=request.POST.get("pati")
        reffer=request.POST.get("reffer")
        freffer=doctor_details.objects.get(id=reffer)
        pr=patient_reports(id=reffer)
        pr.patient_id=fpid
        pr.patient_report_name=patient
        pr.report_file=report
        pr.report_date=pati
        pr.refferd_by=freffer
        pr.save()
    return redirect("/apment/patientreportview/")      
    