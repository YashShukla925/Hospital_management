from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login


# Create your views here.
def Home(request):
    return render(request,'home.html')
def Contact(request):
    return render(request,'contact.html')
def About(request):
    return render(request,'about.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctors = Doctor.objects.all()
    patients= Patient.objects.all()
    appointments = Appointment.objects.all()

    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    
    for j in patients:
        p+=1
    
    for k in appointments:
        a+=1
    
    data1 = {'d':d,'p':p,'a':a}
    return render(request,'index.html',data1)
    
    
    

def Login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
               error="yes"
        except:
            error="yes"

    d = {'error':error}
    return render(request,'login.html',d)

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def view_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,"view_doctor.html",d)

def add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['mobile']
        sp = request.POST['special']

        try:
            Doctor.objects.create(name=n,contact=c,specialization=sp)
            error="no"
        except:
            error="yes"

    d = {'error':error}
    return render(request,'add_doctor.html',d)


def delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    do = Doctor.objects.get(id=pid)
    do.delete()
    return redirect('view_doctor')



def view_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,"view_patient.html",d)

def add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        g = request.POST['gender']
        c = request.POST['mobile']
        ad = request.POST['address']

        try:
            Patient.objects.create(name=n,gender=g,contact=c,address=ad)
            error="no"
        except:
            error="yes"
    

    d = {'error':error}
    return render(request,'add_patient.html',d)


def delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    pa = Patient.objects.get(id=pid)
    pa.delete()
    return redirect('view_patient')




def view_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    d = {'app':app}
    return render(request,"view_appointment.html",d)

def add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']

        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=da,time1=t)
            error="no"
        except:
            error="yes"
    

    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)


def delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    ap = Appointment.objects.get(id=pid)
    ap.delete()
    return redirect('view_appointment')
