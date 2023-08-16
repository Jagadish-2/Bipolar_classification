from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PatientReg

from doctor.models import BipolarReport

import sqlite3
from django.contrib.auth.models import auth
from django.contrib import messages
loginUser = ""
loginFlag = False

# Create your views here.
def home(request):
    return render(request,'patient/log.html')
def register(request):
    return render(request,'patient/reg.html')
def login2(request):
    return render(request,'patient/log.html')

def pregister(request):
    if request.method == 'POST':
        full_name = request.POST['fname']
        pemail2 = request.POST['pemail']
        ppassword = request.POST['Ppassword']
        phoneno = request.POST['phone']
        address = request.POST['address']
        #report1 = "COPD.pdf"
        #reportof1 = "Copd"
        #doctornm1 = "kaisher"
        new_reg = PatientReg(pname=full_name,pemail=pemail2,pphone=phoneno,password=ppassword,paddress=address)
        new_reg.save()
        '''a = PatientReg.objects.get(pemail=pemail2)
        a.report = report1
        a.reportof = reportof1
        a.doctornm = doctornm1
        a.save()'''
        
        
        print("user created") 
        return render(request,'patient/rcomplete.html')
        
    else :
        
        return render(request,'patient/reg.html')

def bipolarReport(request):
    email = request.POST['pemail']
    a = BipolarReport.objects.get(patientemail = email)
    docname1 = a.docname
    reportof1= a.reportof
    reportnm1 = a.reportnm
    Age = a.Age
    Right_answers = a.Right_answers
    Audio_prosody = a.Audio_prosody
    Combined_channel = a.Combined_channel
    Face_video = a.Face_video
    Body_video = a.Body_video
    Positive_valence = a.Positive_valence
    Negative_valence = a.Negative_valence
    Dominant = a.Dominant
    Submissive = a.Submissive
    riskvalue1 = a.riskvalue
    

    return render(request,'patient/bipolarReport.html',{"docname1":docname1,"reportof":reportof1,"download":reportnm1,"a1":Age,
                                                    "b1":Right_answers,"c1":Audio_prosody,"d1":Combined_channel,
                                                    "e1":Face_video,"f1":Body_video,"g1":Positive_valence,"h1":Negative_valence,"i1":Dominant,"j1":Submissive,"data":riskvalue1,"pemail1":email})



    


def login(request):
    #email = request.POST['email']
    #password = request.POST['password']
    
    '''preg =PatientReg.objects.all()
    if(preg.pemail == email and preg.password == password):

        return render(request,'patient/test.html')
    else:
        return render(request,'patient/home.html')'''
    global loginFlag,loginUser
    if request.method == 'POST':
        username = request.POST['email']
        password2 = request.POST['password']

        print(username,password2)
        message = ""

        if len(PatientReg.objects.filter(pemail=username)) == 1 and len(PatientReg.objects.filter(pemail=username))  == 1:
            message = message + "Login successful"
            #mail = username
            #a= PatientReg.objects.exclude(pemail = "username")
            #mail = a.pname
            a=PatientReg.objects.get(pemail = username)
            fname = a.pname
            email = a.pemail

            flag = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
            flag5 = 0
            
            if len(BipolarReport.objects.filter(patientemail=username)) == 1:
                flag5 = 1
            else:
                flag5 = 0

            #copd1 = copd.objects.get(patientemail=username)
            #report = copd1.reportnm

            return render(request,'patient/reportpage.html',{"b":fname,"flag":flag,"flaglung":flag2,"flagdia":flag3,"flagBio":flag5,"flagheart":flag4,"email":email})
        else:
            #pass_hash = str(PatientReg.objects.filter(pemail=username)[0]).split(";")[4]
            #decrypt_text = pass_hash
            #message = message + "Wrong Password Entered"
            messages.info(request,'invalid username or password')
            return render(request,"patient/log.html")
                

        print(message)
        context = {"message":message}
        #return render(request,'RTO/login.html',context)
        return render(request,'patient/log.html',context)

    else:
         return render(request,'patient/log.html')



    
