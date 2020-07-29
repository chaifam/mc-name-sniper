# importing the requests library 
import requests 
import json
import ntplib
from time import ctime
from datetime import datetime
from pytz import timezone
def rightNowTime():
	eastern = timezone('US/Eastern')
	c = ntplib.NTPClient()
	# Provide the respective ntp server ip in below function
	response = c.request('us.pool.ntp.org', version=1)
	response.offset
	now = datetime.fromtimestamp(response.tx_time, eastern)

	

username = input("Whats your username?\n")
password = input("How about your password:\n")
usernameid = input("whats your UUID?\n")
newname = input("what name do you wanna snipe? \n")
time = input("what time does the name become available?\n")
print(rightNowTime())


username = input("Whats your username?\n")
password = input("How about your password:\n")
usernameid = input("What's your UUID?\n")
newname = input("What name do you wanna snipe? \n")
time = input("What time does the name become available?\n")
real_time = rightNowTime


data = json.dumps({"agent":{"name":"Minecraft","version":1},"username":username,"password":password,"clientToken":""})
headersforat = {'Content-Type': 'application/json'}
data = requests.post('https://authserver.mojang.com/authenticate', data=data, headers=headersforat)

pullData = data.json()
AT = pullData["accessToken"]
# api-endpoint 
URL = "https://api.mojang.com/user/profile/"
URL2 = "/skin"  
headers = {"Authorization": "Bearer "+AT}
data = {"model":"", "url":"http://assets.mojang.com/SkinTemplates/steve.png"}
# defining a params dict for the parameters to be sent to the API 

  
# sending get request and saving the response as response object 
r = requests.post(url =  URL+usernameid+URL2, headers = headers, data=data) 

print("the sniper ducked")