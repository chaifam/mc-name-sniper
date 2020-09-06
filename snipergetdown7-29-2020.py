# importing modules
import requests 
import random
import json
import ntplib
import datetime
import time
import threading
import sys
from colorama import init
from bs4 import BeautifulSoup as bs
from termcolor import colored
from datetime import timedelta
from time import ctime
from pytz import timezone

init()

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

#pulls proxies from list of online proxies
def pullProxyList():
	url = "https://www.sslproxies.org/"
	r = requests.get(url)
	soup = bs(r.content, 'html5lib')
	return {'https': random.choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), 
																	  map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

#framework to send proxy requests 1 by 1
def sendProxyRequest(request_type, url, **kwargs):
    while 1:
        try:
            proxy = pullProxyList()
            response = requests.request(request_type, url, proxies=proxy, timeout=1.5, **kwargs)
            break
        except Exception as e:
            pass
    return proxy

# creates session item to make program better
def getSession(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

#framework for sending requests through proxies
def spamMojang():
	for dict_item in proxyList:
		# construct an HTTP session
		session = requests.Session()
		# choose one random proxy
		proxy = dict_item
		session.proxies = proxy
		s = session
		t = datetime.datetime.now()
		r = s.post(url = URL+usernameid+URL2, headers = headers, data = data2, timeout = 5)
		if not r:
			print(colored("REQUEST FAILED[{}]\n", "red").format(dict_item))
			print("Current Time =", t)
		else:
			print(colored("REQUEST SUCCESSFUL[{}]\n", "green").format(dict_item))
			print("You got the name!\n")
			print("Current Time =", t)
			sys.exit()

#tests each proxy and adds it to a dictionary
def makeProxyDict(l):	
	while True:
		item = sendProxyRequest("get", "https://youtube.com")
		try:
			if item not in l:
				l.append(item)
				print("Using proxy: ", item)
		except:
			continue
		else:
			break

#sets times for program to sleep and wake up in order to snipe the name at the right time
def scheduler():
	now = rightNowTime()
	time1_str = (now[:23])
	time2_str = (date_entry + " " + time_entry)
	time1 = datetime.datetime.strptime(time1_str, '%Y-%m-%d %H:%M:%S.%f')
	time2 = datetime.datetime.strptime(time2_str, '%Y-%m-%d %H:%M:%S')
	print("The current time is: {}".format(time1))
	print("The goal time is: {}".format(time2))
	timeDiff = (time2 - time1)
	seconds = timeDiff.total_seconds()
	businessTime = seconds/60
	totalMinutes = str(datetime.timedelta(minutes=businessTime))
	print("{} till snipe".format(totalMinutes))
	if seconds > 1800:
		wait = seconds - 1800
		print(colored("Good for you for planning ahead!", "yellow"))
		time.sleep(wait)
	elif seconds <= 1800:
		print(colored("I could use a little more notice...", "purple"))
		pass
	else:
		print(colored("You are too late. You don't even deserve a special color."))
		sys.exit()

username = input("Enter your current name:\n").strip()	
newname = input("Enter the name you want to snipe: \n").strip()
password = input("Enter your Mojang password:\n").strip()
AT = input("Enter your Bearer Token\n")
date_entry = input('Enter the date the name becomes available in YYYY-MM-DD format:\n').strip()
time_entry = input("Enter the time of day the name becomes available in HH:MM:SS format:\n").strip()

scheduler()

proxyList = []

print(colored("Gathering proxies, this may take a while...", "cyan"))

for b in range(15):
	threading.Thread(target=makeProxyDict(proxyList)).start()

print(proxyList)

a = 0

#for i in range(10):
#	pingteststart = time.perf_counter()
#	pingtest = requests.post(url = "https://api.mojang.com/user/profile/24c182c6716b47c68f60a1be9045c449/name") 
#	pingtestend = time.perf_counter()
#	a += (pingtestend - pingteststart)
#	print(pingtestend-pingteststart)
#average_ping = a/10
#print("Average ping to Mojang servers: {} \n".format(average_ping))


usernameidreq = requests.get(url = "https://api.mojang.com/users/profiles/minecraft/"+username)
jsonusernameid = usernameidreq.json()
usernameid = jsonusernameid["id"]
print(usernameid)
#Justins code (magic)
x = rightNowTime() 
date_time_2_str = (date_entry + " " + time_entry)
date_2 = datetime.datetime.strptime(date_time_2_str, '%Y-%m-%d %H:%M:%S')
date_time_1_str = (x[:23])
date_1 = datetime.datetime.strptime(date_time_1_str, '%Y-%m-%d %H:%M:%S.%f')
print("The current time is: {}".format(date_1))
print("The goal time is: {}".format(date_2))
time_delta = (date_2 - date_1)
total_seconds = time_delta.total_seconds()
clock = total_seconds/60
result = str(datetime.timedelta(minutes=clock))
print("{} till snipe".format(result))
time.sleep(total_seconds - 2)
print("The sniper scopes in (1/2)") #tells you first part of program working




# setting up url to change name 
time0 = time.perf_counter();
URL = "https://api.mojang.com/user/profile/"
URL2 = "/name"  
headers = {"Authorization": "Bearer "+AT, 'User-Agent': useragent}
data2 = json.dumps({"name": newname, "password":password})

# sending get request and saving the response as response object 
for n in range(10):
	threading.Thread(target=spamMojang).start()

time1 = time.perf_counter();
timetoprocess = str(time1-time0)
print("the sniper shot (2/2), it took " + timetoprocess + " seconds to send the requests!") 
sys.exit()
# program has successfully executed. go check your account!