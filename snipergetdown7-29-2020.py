# importing apis
import requests 
import json
import ntplib
import datetime
import time
from datetime import timedelta
from time import ctime
from pytz import timezone

# pulling time from official ntp server
def rightNowTime():
    eastern = timezone('US/Eastern')
    c = ntplib.NTPClient()
    # Provide the respective ntp server ip in below function
    response = c.request('us.pool.ntp.org', version=1)
    response.offset
    now = datetime.datetime.fromtimestamp(response.tx_time, eastern)
    return str(now)

    
# asking user to input information
username = input("Enter your Mojang e-mail/username:\n").strip()
password = input("Enter your Mojang password:\n").strip()
usernameid = input("Enter your UUID:\n").strip()
newname = input("Enter the name you want to snipe: \n").strip()
date_entry = input('Enter the date the name becomes available in YYYY-MM-DD format:\n').strip()
time_entry = input("Enter the time of day the name becomes available in HH:MM:SS.mmmmmm format:\n").strip()

#logging in to the MC server and returning an access token
data = json.dumps({"agent":{"name":"Minecraft","version":1},"username":username,"password":password,"clientToken":""})
headersforat = {'Content-Type': 'application/json'}
data = requests.post('https://authserver.mojang.com/authenticate', data=data, headers=headersforat)

pullData = data.json()
AT = pullData["accessToken"]

#Justins code (magic)
x = rightNowTime() 
date_time_2_str = (date_entry + " " + time_entry)
date_2 = datetime.datetime.strptime(date_time_2_str, '%Y-%m-%d %H:%M:%S.%f')
date_time_1_str = (x[:23])
date_1 = datetime.datetime.strptime(date_time_1_str, '%Y-%m-%d %H:%M:%S.%f')
print("The current time is: {}".format(date_1))
print("The goal time is: {}".format(date_2))
time_delta = (date_2 - date_1)
total_seconds = time_delta.total_seconds()
minutes = total_seconds/60
print("{} minutes till snipe".format(minutes))
print("The sniper scopes in (1/2)") #tells you first part of program working
time.sleep(total_seconds)



# setting up url to change name 
URL = "https://api.mojang.com/user/profile/"
URL2 = "/name"  
headers = {"Authorization": "Bearer "+AT}
data2 = json.dumps({"name": newname, "password":password})


  
# sending get request and saving the response as response object 
r = requests.post(url =  URL+usernameid+URL2, headers = headers, data=data2) 
print (r.status_code + r.error+ r.text)
print("the sniper shot (2/2)") 

# program has successfully executed. go check your account!