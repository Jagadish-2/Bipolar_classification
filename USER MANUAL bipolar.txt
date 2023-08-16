step 1:
-->installing all the requires packages
*open anaconda anigator
*open cmd.exe prompt
-> 	install reauired packages
		-pip install python
		-pip install tensorflow
		-pip install django
		-pip install flask
		-pip install dash

step 2:
*open cmd.exe and navigate to sleepRes.py
path: Desktop->Bipolarcassification->sleep final->python sleepRes.py

step 3:
*open cmd.exe and navigate to flask_api.py
path: Desktop->Bipolarcassification->bipolar->python flask_api.py

step 4:
*open cmd.exe and navigate to manage.py
path: Desktop->Bipolarcassification->python manage.py runserver

step 5:
*copy the url and past it in a browser
*http://127.0.0.1:8000/doctor/   (opens doctor module)
http://127.0.0.1:8000/patient/   (opens patient module)



USER MANUAL 
Doctor module: 
step 1: log into Bipolar and sleep apnea detection 
step 2: A new doctor can register 
step 3: select the disorder 
step 4: Bipolar detection needs patient information for prediction 
step 5: Sleep Apnea needs EEG data from the patient 
step 6: Click on submit to get the prediction 
step 7: Doctor can view the report  

Patient module: 
step 1: log into the Patient module 
step 2: A new patient can register 
step 3: patient can take the bipolar test 
step 4: After the test is completed the patient can view the report 
step 5: The patient can download the report

bipolar test: 
step 1: log into the Patient module 
step 2: select the bipolar test in the patient module 
Step 3: Answer the questions in the bipolar test 
step 4: test results will be displayed 
step 5: if tested positive it will prompted to meet a doctor. 

sleep Apnea detection: 
step 1: log into Bipolar and sleep apnea detection 
step 2: click on sleep apnea detection 
step 3: upload the EEG data
step 5: click on submit 
Step 6: sleep apnea is predicted
