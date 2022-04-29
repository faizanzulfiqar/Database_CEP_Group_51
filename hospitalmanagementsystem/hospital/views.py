from django.shortcuts import render
from django.http import HttpResponse
from numpy import save
from hospital.models import Patient, Staff
from hospital.models import Doctor
from django.contrib import messages

def homepage(request):
    return render(request , 'index.html')
def aboutpage(request):
    return render(request, 'about.html')
def loginpage(request):
    return render(request, 'login.html')
def createaccountpage(request):
    return render(request, 'createaccount.html')


def InsertPatientRecord(request):
    if request.method=='POST':
        if request.POST.get('patient_id') and request.POST.get('f_name'):
            saverecord=Patient()
            saverecord.patient_id=request.POST.get('patient_id')
            saverecord.f_name=request.POST.get('f_name')
            saverecord.l_name=request.POST.get('l_name')
            saverecord.address=request.POST.get('address')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully!')
            return render(request,'Patient.html')
    else:
        return render(request,'Patient.html')



def InsertStaffRecord(request):
    if request.method=='POST':
        if request.POST.get('staff_id') and request.POST.get('fname'):
            saverecord=Staff()
            saverecord.staff_id=request.POST.get('staff_id')
            saverecord.fname=request.POST.get('fname')
            saverecord.lname=request.POST.get('lname')
            saverecord.phone_no=request.POST.get('phone_no')
            saverecord.address=request.POST.get('address')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully!')
            return render(request,'Staff.html')
    else:
        return render(request,'Staff.html')