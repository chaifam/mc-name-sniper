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
	return(now)

	

username = input("Whats your username?\n").strip()
password = input("How about your password:\n").strip()
usernameid = input("whats your UUID?\n").strip()
newname = input("what name do you wanna snipe? \n").strip()
snipeYear = input("What year is it?\n").strip()
snipeMonth = input("What month does the name become available?\n").strip()
snipeDay = input("What day does the name become available?\n").strip()
snipeTime = input("What time does the name become available? (HOUR:MINUTE:SECOND)\n").strip()
text = ("{}-{}-{} {}").format(snipeYear, snipeMonth, snipeDay, snipeTime)
print(text)



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


  
# sending get request and saving the response as response object 
r = requests.post(url =  URL+usernameid+URL2, headers = headers, data=data) 

print("the sniper ducked")