from flask import Flask, render_template, url_for, request
import sqlite3
#from A_Recognition import analyse
import os
from flask import Flask, render_template, request, send_file ,jsonify
from gtts import gTTS
from mutagen.mp3 import MP3
import pygame
import time
import os
import speech_recognition as sr
import pyttsx3
import uuid



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result)==0:
            return render_template('index.html',msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            return render_template('userlog.html')

    return render_template('home.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/userlog.html')
def user():
    return render_template('userlog.html')



#Words Recognition

@app.route('/Live1', methods=['GET', 'POST'])
def Live1():
   
        
    os.system('python wordrecognition.py')
    return render_template('userlog.html')


#Numbers Recognition

@app.route('/Live2', methods=['GET', 'POST'])
def Live2():
   
        
    os.system('python number.py')
    return render_template('userlog.html')




#Object Detection   

@app.route('/Live4', methods=['GET', 'POST'])
def Live4():
    
        
    os.system('python main.py')
    return render_template('userlog.html')
   




if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")

    app.run(debug=True, use_reloader=False)
