# importing the requests library 
import requests 
import json
import ntplib
from time import ctime

c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org', version=3)
print(ctime(response.tx_time))


username = input("Whats your username?\n")
password = input("How about your password:\n")
usernameid = input("whats your UUID?\n")
data = json.dumps({"agent":{"name":"Minecraft","version":1},"username":username,"password":password,"clientToken":""})
headersforat = {'Content-Type': 'application/json'}
data = requests.post('https://authserver.mojang.com/authenticate', data=data, headers=headersforat)

pullData = data.json()
AT = pullData["accessToken"]
# api-endpoint 
URL = "https://api.mojang.com/user/profile/"
URL2 = "/skin"  
# location given here 

headers = {"Authorization": "Bearer "+AT}
data = {"model":"", "url":"http://assets.mojang.com/SkinTemplates/steve.png"}
# defining a params dict for the parameters to be sent to the API 

  
# sending get request and saving the response as response object 
r = requests.post(url =  URL+usernameid+URL2, headers = headers, data=data) 

print("the sniper ducked")