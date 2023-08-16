from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS
from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
from flask import *
import json
#import MySQLdb

mydb = mysql.connector.connect(user='root', password='root',host='localhost',database='bipolar')
#dbconn = MySQLdb.connect(user='root', password='root',host='localhost',database='bipolar')
app = Flask(__name__)
app.secret_key='bipolar'
CORS(app)
api = Api(app)
app.static_folder = 'static'

@app.route('/')
def index():
   return render_template('index.html')



@app.route('/user_login')
def user_login():
   return render_template('user_login.html')


@app.route('/user_signup')
def user_signup():
   return render_template('user_signup.html')

@app.route('/bipolar')
def bipolar():
   print('testing bipolar')
   return render_template('bipolar.html')


@app.route('/user_home')
def user_home():
   return render_template('user_home.html')

@app.route('/bipolar_msg')
def bipolar_msg():
   print("bipolar msg...")
   return render_template('bipolar_msg.html')





  


@app.route('/logout')  
def logout():  
    if 'id' in session:  
        session.pop('id',None)
        session.pop('mobile',None)
        session.pop('name',None) 
        return render_template('index.html');  
    else:  
        return '<p>user already logged out</p>' 



class user_login_check(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('user', required=True)  # add args
        parser.add_argument('pass', required=True)  # add args
        
        
        args = parser.parse_args()  # parse arguments to dictionary
        print('user',args['user'])
        print('pass',args['pass'])
        sql = "SELECT * FROM user_details WHERE email = %s and pass= %s"
        det = (args['user'], args['pass'])
        mycursor = mydb.cursor()

        mycursor.execute(sql, det)

        myresult = mycursor.fetchall()
        id=''
        name=''
        mobile=''
        email=''
        mycursor.close()

        for x in myresult:
           print(x)
           id=x[0]
           name=x[1]
           mobile=x[3]
           address=x[4]
        if id!='':
           session['id']=id
           session['mobile']=mobile
           session['name']=name
           session['address']=address
           return str(id)+'#'+str(mobile)+'#'+str(name)
        else:
           return "not matching"




class add_user(Resource):
    
        
        
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('name', required=True)  # add args
        parser.add_argument('email', required=True)  # add args
        parser.add_argument('mobile', required=True)  # add args
        parser.add_argument('pass', required=True)  # add args
        parser.add_argument('address', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
       
        print('name',args['name'])
        print('email',args['email'])
        print('mobile',args['mobile'])
        print('pass',args['pass'])
        print('address',args['address'])
        sql = "INSERT INTO user_details (name, email,mobile,address,pass) VALUES (%s, %s,%s, %s,%s)"
        val = (args['name'], args['email'],args['mobile'],args['address'],args['pass'])
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Regitered.")
        mycursor.close()
        
        return "Registered"



    





api.add_resource(add_user, '/add_user')
api.add_resource(user_login_check, '/user_login_check')


if __name__ == '__main__':
    app.run()  # run our Flask app
