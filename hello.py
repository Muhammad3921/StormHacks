from flask import Flask, render_template, request, url_for, redirect
import numpy as np
from numpy.random import seed
from numpy.random import randint
import itertools
import os
from twilio.rest import Client
app = Flask(__name__)
account_sid = 'AC5abec30cd213fff77859a055f6099d8f'
auth_token = '63eb7f2c4859e0d8240356ade6a1f816'
client = Client(account_sid, auth_token)


@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def hello():
  return render_template('home.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/payment',methods=['GET', 'POST'])
def payment():
     if request.method == "POST":
        return render_template('login.html')
     else:
        return render_template('payment.html')
    

@app.route('/login',methods=['GET', 'POST'] )
def log():
     if request.method == "POST":
        return redirect("/forms", code=302)
     else:
        return render_template('login.html')

@app.route('/setup',methods=['GET', 'POST'] )
def set():
     if request.method == "POST":
        return redirect("/payment", code=302)
     else:
        return render_template('setup.html')

@app.route('/forms',methods=['GET', 'POST'])
def formsss():
    lvlInput = "lol"
    equipArr = [None]*10
    daysTime = [None]*7
    daysFocus = [None]*7
    count = 0
    # equipmentArr = ["Treadmill", "Resistence Bands", "Resistence Band Loops", "Yoga Mat",
              #  "Dumbells", "Bench Press", "Pull Up Bar", "Kettle Bell", "Jump Rope", "NONE"] 

    if request.method == "POST":
        lvlInput = request.form["trai"]
        phone = request.form["phone"]
        if(request.form.get("tred")):
            equipArr[0] = 1
            count = count + 1
        else:
            equipArr[0] = 0
        if(request.form.get("reis")):
            equipArr[1] = 1
            count = count + 1
        else:
            equipArr[1] = 0
        if(request.form.get("loo")):
            equipArr[2] = 1
            count = count + 1
        else:
            equipArr[2] = 0
        if(request.form.get("yoga")):
            equipArr[3] = 1
            count = count + 1
        else:
            equipArr[3] = 0
        if(request.form.get("dumb")):
            equipArr[4] = 1
            count = count + 1
        else:
            equipArr[4] = 0
        if(request.form.get("press")):
            equipArr[5] = 1
            count = count + 1
        else:
            equipArr[5] = 0
        if(request.form.get("pull")):
            equipArr[6] = 1
            count = count + 1
        else:
            equipArr[6] = 0
        if(request.form.get("kettle")):
            equipArr[7] = 1
            count = count + 1
        else:
            equipArr[7] = 0
        if(request.form.get("jump")):
            equipArr[8] = 1
            count = count + 1
        else:
            equipArr[8] = 0
        if(request.form.get("none")):
            equipArr[9] = 1
            count = count + 1
        else:
            equipArr[9] = 0
            
        daysTime[0] = request.form["mt"]
        daysTime[1] = request.form["tt"]
        daysTime[2] = request.form["wt"]
        daysTime[3] = request.form["tht"]
        daysTime[4] = request.form["ft"]
        daysTime[5] = request.form["sat"]
        daysTime[6] = request.form["sut"]
        
        daysFocus[0] = request.form["mw"]
        daysFocus[1] = request.form["tw"]
        daysFocus[2] = request.form["ww"]
        daysFocus[3] = request.form["thw"]
        daysFocus[4] = request.form["fw"]
        daysFocus[5] = request.form["saw"]
        daysFocus[6] = request.form["suw"]

            #this is for getting the number for training level
        level = ["Beginner","Intermediate","Advanced"]
        levelVal = 0
        for i in range(len(level)):
            if(lvlInput == level[i]):
                levelVal = i+1
                break
        
        # convert equipment to array of integers that user has
        equipmentList = [None]*count 
        counter = 0
        for i in range(len(equipArr)):
            if(equipArr[i] == 1):
                equipmentList[counter] = i+1
                counter = counter + 1

        days = ["MON", "TUES", "WED", "THURS", "FRI","SAT", "SUN"]
        areaArr = ["Chest", "Back", "Arms", "Abs", "Legs", "Shoulders", "Cardio", "Calves", "Glutes",
            "Forearms", "Quads", "Triceps"]
        daysArr = [None]*7
        timings = ["0-10","10-15","15-20","20-30","30+"]

        for j in range(len(days)): 
            # convert days time to integer
            timingVal = 0
            for i in range(len(timings)):
                if(daysTime[j] == timings[i]):
                    dayVal = i+1
                    break
            
            focusVal = 0
            for i in range(len(areaArr)):
                if(daysFocus[j] == areaArr[i]):
                    focusVal = i+1
                    break
            a = [[levelVal],equipmentList, [dayVal],[focusVal]]
            b = list(itertools.product(*a))

            
            for i in range(len(b)):
                codeStr = str(b[i][0]) +  str(b[i][1]) + str(b[i][2]) + str(b[i][3]) 
                b[i] = int(codeStr)

            daysArr[j] = b
        
        equipmentAll = ["Treadmill", "Resistence Bands", "Resistence Band Loops", "Yoga Mat",
                "Dumbells", "Bench Press", "Pull Up Bar", "Kettle Bell", "Jump Rope", "NONE"]
        weeklyEquip = [None]*7
        equipAvailable = [None]*count
        for i in range(count):
            equipAvailable[i] = equipmentAll[equipmentList[i]-1]

        for i in range(len(weeklyEquip)):
            value = randint(0,count)
            weeklyEquip[i] = equipAvailable[value]
        
        # daysFocus
        # weeklyEquip contains 7 strings of equipment the user has in random order

        
        
        

        
         
        message = client.messages \
                .create(
                     body="Thank you for registering with HomeWxrkOuts, we look forward to providing you with a fitness regimen to keep you healthy!",
                     from_='+12517584511',
                     to=phone
                 )

        print(message.sid)
        
        return render_template('videos.html', eq = weeklyEquip , re = daysFocus)   
    else: 
        return render_template('forms.html')

 

@app.route('/about')
def about():
    return render_template('about.html')

    

if __name__ == "__main__":
  app.run() 