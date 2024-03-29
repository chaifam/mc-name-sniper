# importing modules
import requests 
import random
import json
import ntplib
import datetime
import time
import threading
import sys
import os
import concurrent.futures
import re
from mojang import MojangUser, MojangAPI, MojangSession
from mojang.exceptions import SecurityAnswerError
from colorama import init
from bs4 import BeautifulSoup as bs
from termcolor import colored
from datetime import timedelta
from time import ctime
from pytz import timezone


init()

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

with open("config.json", "r") as f:
	config = json.load(f)




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
def pullProxyList(proxyUrl):
	url = proxyUrl
	r = requests.get(url)
	soup = bs(r.content, 'html5lib')
	return {'https': random.choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), 
																		  map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

#framework to send proxy requests 1 by 1
def proxyTest():
	while True:
		try:
			with concurrent.futures.ThreadPoolExecutor() as executor:	
				urls = ["https://free-proxy-list.net/", "https://www.sslproxies.org/"]
				results = [executor.submit(pullProxyList, url) for url in urls]
				for f in concurrent.futures.as_completed(results):
					proxy = f.result()
					testUser = MojangUser(config["name"], config["password"], proxy = proxy["https"])
					response = testUser._validate_proxy()
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


#tests each proxy and adds it to a dictionary
#def makeProxyDict(l):	
#	item = proxyTest("get", "https://www.minecraft.net/en-us")
#	while True:	
#		try:
#			if item not in l and re.search('[a-zA-Z]', item["https"]) == None:
#				l.append(item)
#				print(item)
#		except:
#			continue
#		else:
#			break
def makeProxyDict(l):	
	while True:	
		try: 
			item = proxyTest("get", "https://api.mojang.com/", timeout=10)
			#and re.search("[a-zA-Z_-]", item["https"]) == None:
			if proxy not in l:
				l.append(proxy)
				print(proxy)
		except:
			continue
		else:
			break

def getAT():
	#gets access token from mojangs authentication servers using mikis huge brain
	jsonForAT = json.dumps({"agent":{"name":"Minecraft","version":1},"username":email,"password":password,"clientToken":""})
	headersForAT = {'Content-Type': 'application/json'}
	requestForAT = requests.post('https://authserver.mojang.com/authenticate', data=jsonForAT, headers=headersForAT)

	pullATRequestData = requestForAT.json()
	AT = pullATRequestData["accessToken"]
	print("Your access token is "+AT+" lol not that you care")
	return AT

#sets times for program to sleep and wake up in order to snipe the name at the right time
def scheduler():
	drop_timestamp = MojangAPI.get_drop_timestamp()

	if not drop_timestamp:
		print(f"{newname} is not dropping")
	else:
		dropSeconds = drop_timestamp - time.time()
		print(f"{newname} drops in {dropSeconds} seconds")
		totalMinutes = str(datetime.timedelta(minutes=dropSeconds))
		print("{} till snipe".format(totalMinutes))
		if seconds > 180:
			wait = dropSeconds - 180
			print(colored("I'll do my best!", "yellow"))
			time.sleep(wait)

		elif dropSeconds <= 180:
			print(colored("You're really putting me on a time crunch...", "magenta"))
			pass
		else:
			print(colored("You are too late. You don't even deserve a special color."))
			sys.exit()

def sniperBullet(plist):
	try:
		user = MojangUser(config["name"], config["password"], proxy = plist["https"])

		if not user.is_fully_authenticated: 
			# print the security challenges if you need them
			print(user.security_challenges)
			
			# make a list of the 3 answers to send
			# make sure they are in the same order as the challenges
			# they are not case-sensitive
			answers = ["security"]
			
			# completes authentication
			# throws SecurityAnswerError if a question is incorrect
			try:
				user.answer_security_challenges(answers)
			except SecurityAnswerError:
				print("A security answer was answered incorrectly.")
		if not user.profile.is_name_change_allowed:
			print("Account does not have an available name change")
			print(f"It was last changed on {user.profile.name_changed_at}")
	if user.profile.change_name(newname) == True:
		t = datetime.datetime.now()
		str1 = colored("REQUEST SUCCESSFUL[{}]", "green").format(plist)
		str2 = colored(t, "cyan")
		print(r.status_code, r.text)
		return str1 + " @ " + str2 + "\n"
	else:
		t = datetime.datetime.now()
		str1 = colored("REQUEST FAILED[{}]", "red").format(plist)
		str2 = colored(t, "cyan")
		print(r.status_code, r.text)
		return str1 + " @ " + str2 + "\n"
		



#framework for sending requests through proxies
def spamMojang():
	# setting up url to change name 
	with concurrent.futures.ThreadPoolExecutor() as executor:
		spamResults = executor.map(sniperBullet, proxyList)
		for spamResult in spamResults:
			print(spamResult)
	

username = config["name"]	
email = config["email"]	
password = config["password"]
newname = input("Enter the name you want to snipe: \n").strip()

print(username)
print(email)
print(password)
print(newname)
usernameidreq = requests.get(url = "https://api.mojang.com/users/profiles/minecraft/"+username)
jsonusernameid = usernameidreq.json()
usernameid = jsonusernameid["id"]
print(usernameid)

try:
	user = MojangUser(config["name"], config["password"], proxy = plist)

	if not user.is_fully_authenticated: 
		# print the security challenges if you need them
		print(user.security_challenges)
		
		# make a list of the 3 answers to send
		# make sure they are in the same order as the challenges
		# they are not case-sensitive
		answers = ["security"]
		
		# completes authentication
		# throws SecurityAnswerError if a question is incorrect
		try:
			user.answer_security_challenges(answers)
		except SecurityAnswerError:
			print("A security answer was answered incorrectly.")
	if not user.profile.is_name_change_allowed:
		print("Account does not have an available name change")
		print(f"It was last changed on {user.profile.name_changed_at}")


scheduler()

proxyList = []

print(colored("Gathering proxies, this may take a while...", "cyan"))


t1 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
	results = [executor.submit(makeProxyDict, proxyList) for _ in range(15)]
t2 = time.perf_counter()
proxyTime = t2-t1
print(f"It took {proxyTime} seconds to gather proxies.")


print(proxyList)

a = 0


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
print("The sniper scopes in (1/2)") #tells you first part of program working
time.sleep(total_seconds - 5)


time0 = time.perf_counter()

# sending get request and saving the response as response object 
with concurrent.futures.ProcessPoolExecutor() as executor:
	numberRequests = round(600/len(proxyList))
	for n in range(numberRequests):	
		executor.map(spamMojang())

#for n in range(10):
#	threading.Thread(target=spamMojang).start()

time1 = time.perf_counter();
timetoprocess = str(time1-time0)
print("the sniper shot (2/2), it took " + timetoprocess + " seconds to send the requests!") 
sys.exit()
# program has successfully executed. go check your account!