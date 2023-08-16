from django.contrib import messages


from django.views.generic.detail import DetailView
from patient.models import PatientReg
from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image,Spacer
#creating the reportlab pdf library here.
import time
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
#creating the CNN library from here

import datetime


#importing the smtp
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
#creating the reportlab pdf library here.
import time
from reportlab.lib.enums import TA_JUSTIFY

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
# Create your views here.
def reg(request):
    return render(request,"doctor/reg.html")
def index(request):
    return render(request,"doctor/index.html")
def home(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid username or password!')
            return render(request,"doctor/log.html")
    
    else :        

        return render(request,"doctor/log.html")    
    return render(request,'doctor/log.html')

def login(request):

   #suppose if we post the data 
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid username or password')
            return render(request,"doctor/log.html")
    
    else :        

        return render(request,"doctor/log.html")    
    #return render(request,'doctor/home.html')
#def register(request):
#    return render(request,'doctor/register.html')

def login2(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"doctor/option.html")
        else :
            messages.info(request,'invalid username or password')
            return render(request,"doctor/log.html")
    
    else :        

        return render(request,"doctor/log.html")    
    return render(request,'doctor/log.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email1=request.POST['email']
        email2=request.POST['email2']
        password1=request.POST['password']
        password2=request.POST['password2']
        if password1 == password2 and email1 == email2:
            if User.objects.filter(username=email1):
                #print("Username is taken")
                messages.info(request,'Username is taken')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username=email1, password = password1, email = email1, first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            #print("Password not matching or email is not matching")
            messages.info(request,'Password not matching or email is not matching')
            return redirect('register')
        #return HttpResponse("<script>alert('User created')</script>")
        return render(request,'doctor/registerComplet.html')
    
    else :
        
        return render(request,'doctor/reg.html')

def rcomplete(request):
    return render(request,'doctor/registerComplet.html')


def bipolar(request):
    return render(request,'doctor/bipolarReport.html')










def predBipolar(request):
    if request.method == 'POST':
        a = request.POST['Age']
        b = request.POST['Right_answers']
        c = request.POST['Audio_prosody']
        d = request.POST['Combined_channel']
        e = request.POST['Face_video']
        f = request.POST['Body_video']
        
        g = request.POST['Positive_valence']
        h = request.POST['Negative_valence']
        i = request.POST['Dominant']
        j = request.POST['Submissive']
        pemail1 = request.POST['pemail']
        docname1 = request.POST['docname']
        reportof = request.POST['reportof']
        
        lists =[a,b,c,d,e,f,g,h,i,j]
        df = pd.read_csv(r"static/database/Bipolar.csv")
        X_train = df[['Age', 'Right_answers', 'Audio_prosody', 'Combined_channel', 'Face_video','Body_video','Positive_valence','Negative_valence','Dominant','Submissive']]
        
        Y_train = df[['Type']]
        tree = DecisionTreeClassifier(max_leaf_nodes=6, random_state=0)
        
        tree.fit(X_train, Y_train)
        prediction = tree.predict([[a,b,c,d,e,f,g,h,i,j]])
        
        return render(request,'doctor/predictBipolar.html',{"data":prediction,"lists":lists,"a1":a,"b1":b,"c1":c,"d1":d,"e1":e,"f1":f,"g1":g,"h1":h,"i1":i,"j1":j,"pemail1":pemail1,"docname1":docname1,"reportof":reportof})
    
    return render(request, 'doctor/predictBipolar.html')

def bipolarSv(request):
    #this is where error id popping
    a1 = request.POST['Age']
    b = request.POST['Right_answers']
    c = request.POST['Audio_prosody']
    d1 = request.POST['Combined_channel']
    e = request.POST['Face_video']
    f = request.POST['Body_video']
    g = request.POST['Positive_valence']
    h = request.POST['Negative_valence']
    i = request.POST['Dominant']
    j = request.POST['Submissive']
    #k = "nothing"
    pemail1 = request.POST['pemail']
    docname1 = request.POST['docname']
    reportof1 = request.POST['reportof']
    detail = request.POST['data']
     #importing the package in realtime.
    from .models import BipolarReport
    from patient.models import PatientReg
    #importing reportlab
    
    #Genrating the report here
    basename = "BipolarReport"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename2 = "_".join([basename, suffix])
    loc="static/report/"+filename2+".pdf"

    b3 = PatientReg.objects.get(pemail=pemail1)
   
    fname = b3.pname

    #file naming is in above
    doc = SimpleDocTemplate(loc,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/images/seal.png"

    #giving all body of report
    formatted_time = time.ctime()
    full_name = fname
    address_parts = [pemail1]

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="12">%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size="12"></font>' 
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        
        ptext = '<font size="12">%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">We have generated the report of <b> %s</b>, we found the your risk of %s is \
        =<b>%s</b>, we recommend you to care for your health, because your this health will\
        help you to live the happy life. We are attaching the report here</font>' % (reportof1,reportof1,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Patient email = %s    || Doctor name=%s                    \
    </font>' % (pemail1,docname1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Report of = <b>%s  </b>                 \
    </font>' % (reportof1)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    <b>Age</b>= %s     || <b>Right_answers</b>= %s   ||    <b>Audio_prosody</b>=%s             \
    </font>' % (a1,b,c)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>Combined_channel</b>= %s     || <b>Face_video</b>= %s   ||    <b>Body_video</b>=%s             \
    </font>' % (d1,e,f)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))



    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>Positive_valence</b>= %s     || <b>Negative_valence</b>= %s   ||   <b> Dominant</b>=%s             \
    </font>' % (g,h,i)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    ------------------------------------------------------------------------------------------------------------------\
    <b>Submissive</b>= %s     ||                \
    </font>' % (j)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))




    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
    Your rishk about the<b> %s</b>=<b> %s</b>                 \
    </font>' % (reportof1,detail)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">\
    -----------------------------------------------------------------------------------------------------------------\
                \
    </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size="12">Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = '<font size="12">%s</font>' % (docname1)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))





    doc.build(Story)
    #applying the smtp server here
    # fromaddr = "jagadishbob123@gmail.com"
    # toaddr = pemail1
    # msg = MIMEMultipart() 
    # msg['From'] = fromaddr 


    # msg['To'] = toaddr 
    # msg['Subject'] = "This is your report"
    # body = "Kindly check the attachment"
    # msg.attach(MIMEText(body, 'plain')) 


    filename = filename2+".pdf"
    # attachment = open(loc, "rb")
    # p = MIMEBase('application', 'octet-stream') 


    # p.set_payload((attachment).read()) 

 
    # encoders.encode_base64(p) 

    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    # msg.attach(p) 

 
    # s = smtplib.SMTP('smtp-mail.outlook.com', 587) 


    # s.starttls() 

 
    # s.login(fromaddr, "jagadishbob123@gmail.com") 


    # text = msg.as_string() 

 
    # s.sendmail(fromaddr, toaddr, text) 

    # print("Msg sent successful")
    # s.quit()
    #saving the data

    if len(BipolarReport.objects.filter(patientemail=pemail1)) == 1:
        a = BipolarReport.objects.get(patientemail = pemail1)
        a.docname = docname1
        a.reportof = reportof1
        a.reportnm = filename
        a.Age = a1
        a.Right_answers = b
        a.Audio_prosody = c
        a.Combined_channel = d1
        a.Face_video = e
        a.Body_video = f
        a.Positive_valence = g
        a.Negative_valence = h
        a.Dominant = i
        a.Submissive = j 
        a.riskvalue = detail
        a.save()
    else:
        

        d = BipolarReport(patientemail=pemail1,docname=docname1,reportof=reportof1,reportnm=filename,Age=a1,Right_answers=b,Audio_prosody=c,Combined_channel=d1,Face_video=e,Body_video=f,Positive_valence=g,Negative_valence=h,Dominant=i,Submissive=j,riskvalue=detail)
        d.save()





    return render(request,'doctor/sendSuccess.html')
