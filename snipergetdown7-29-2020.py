# importing apis
import requests 
import json
import ntplib
import datetime
import time
from datetime import timedelta
from time import ctime
from pytz import timezone

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'


# pulling time from official ntp server
def rightNowTime():
	eastern = timezone('US/Eastern')
	c = ntplib.NTPClient()
	# Provide the respective ntp server ip in below function
	response = c.request('us.pool.ntp.org', version=1)
	response.offset
	now = datetime.datetime.fromtimestamp(response.tx_time, eastern)
	return str(now)

a = 0

for i in range(10):
	pingteststart = time.perf_counter()
	pingtest = requests.post(url =  "https://api.mojang.com/user/profile/24c182c6716b47c68f60a1be9045c449/name") 
	pingtestend = time.perf_counter()
	a += (pingtestend - pingteststart)
	print(pingtestend-pingteststart)
average_ping = a/10
print("Average ping to Mojang servers: {} \n".format(average_ping))


	
newname = input("Enter the name you want to snipe: \n").strip()
password = input("Enter your Mojang password:\n").strip()
usernameid = input("Enter your UUID:\n").strip()
AT = input("Enter your Bearer Token\n")
date_entry = input('Enter the date the name becomes available in YYYY-MM-DD format:\n').strip()
time_entry = input("Enter the time of day the name becomes available in HH:MM:SS.mmmmmm format:\n").strip()


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
time0 = time.perf_counter();
URL = "https://api.mojang.com/user/profile/"
URL2 = "/name"  
headers = {"Authorization": "Bearer "+AT, 'User-Agent': useragent}
data2 = json.dumps({"name": newname, "password":password})


  
# sending get request and saving the response as response object 
n = 0
while n < (30):
	r = requests.post(url =  URL+usernameid+URL2, headers = headers, data=data2)
	if not r:
		print("REQUEST FAILED [{}]\n".format(i))
		i += 1
	else:
		print("REQUEST SUCCESSFUL [{}]\n".format(i))
		print("You got the name!\n")
		break

print(r.status_code, r.text)
time1 = time.perf_counter();
timetoprocess = str(time1-time0)
print("the sniper shot (2/2), it took " + timetoprocess + " seconds to send the requests!") 
# program has successfully executed. go check your account!