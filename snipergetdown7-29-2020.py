# importing apis
import requests 
import random
import json
import ntplib
import datetime
import time
import threading
from grab import Grab, GrabError
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

#def get_free_proxies():
#	url = ""
#	proxies = []
#	# get the HTTP response and construct soup object
#	soup = bs(requests.get(url).content, "html.parser")
#	for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
#		tds = row.find_all("td")
#		try:
#			ip = tds[0].text.strip()
#			port = tds[1].text.strip()
#			host = f"{ip}:{port}"
#			proxies.append(host)
#		except IndexError:
#			continue
#	return proxies

def get_proxy():
	url = "https://www.sslproxies.org/"
	r = requests.get(url)
	soup = bs(r.content, 'html5lib')
	return {'https': random.choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), 
																	  map(lambda x:x.text, soup.findAll('td')[1::8]))))))}


#def get_session(proxies):
#	# construct an HTTP session
#	session = requests.Session()
#	# choose random proxies
#	proxy = random.choice(proxies)
#	session.proxies = {"http": proxy, "https": proxy}
#	return session

#def get_valid_proxy(proxy_list): #format of items e.g. '128.2.198.188:3124'
#	g = Grab()
#	for proxy in proxy_list:
#		g.setup(proxy=proxy, proxy_type='http', connect_timeout=5, timeout=5)
#		try:
#			g.go('google.com')
#		except GrabError:
#			logging.info("Test error")
#			pass
#		else:
#			yield proxy

def proxy_request(request_type, url, **kwargs):
    while 1:
        try:
            proxy = get_proxy()
            response = requests.request(request_type, url, proxies=proxy, timeout=1.5, **kwargs)
            break
        except Exception as e:
            pass
    return proxy




def g():
	n = 0
	for n in range(10):
		t = datetime.datetime.now()
		r = requests.get(url = URL+usernameid+URL2, headers = headers, data = data2, proxies = dict_item)
		if not r:
			print(colored("REQUEST FAILED[{}]\n", "red").format(dict_item))
			print("Current Time =", t)
			n += 1
		else:
			print(colored("REQUEST SUCCESSFUL[{}]\n", "green").format(dict_item))
			print("You got the name!\n")
			print("Current Time =", t)
			break


def get_proxy_dict(l):	
	while True:
		item = proxy_request("get", "https://youtube.com")
		try:
			if item not in l:
				l.append(item)
				print("Using proxy: ", item)
		except:
			continue
		else:
			break

	

#proxy_choices = get_free_proxies()
#actual_proxy_choices = get_valid_proxy(proxy_choices)
#print(proxy_choices)

proxyList = []

print(colored("Gathering proxies, this may take a while...", "cyan"))

for b in range(50):
	threading.Thread(target=get_proxy_dict(proxyList)).start()

print(proxyList)
# TESTING PURPOSES

#filtered_ip_list = [ip for ip in ip_list if ip != "Backend not available"]



a = 0

for i in range(10):
	pingteststart = time.perf_counter()
	pingtest = requests.post(url = "https://api.mojang.com/user/profile/24c182c6716b47c68f60a1be9045c449/name") 
	pingtestend = time.perf_counter()
	a += (pingtestend - pingteststart)
	print(pingtestend-pingteststart)
average_ping = a/10
print("Average ping to Mojang servers: {} \n".format(average_ping))


	
newname = input("Enter the name you want to snipe: \n").strip()
password = input("Enter your Mojang password:\n").strip()
username = input("Enter your username:\n").strip()
AT = input("Enter your Bearer Token\n")
date_entry = input('Enter the date the name becomes available in YYYY-MM-DD format:\n').strip()
time_entry = input("Enter the time of day the name becomes available in HH:MM:SS format:\n").strip()

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
time.sleep(total_seconds - average_ping)
print("The sniper scopes in (1/2)") #tells you first part of program working




# setting up url to change name 
time0 = time.perf_counter();
URL = "https://api.mojang.com/user/profile/"
URL2 = "/name"  
headers = {"Authorization": "Bearer "+AT, 'User-Agent': useragent}
data2 = json.dumps({"name": newname, "password":password})

# sending get request and saving the response as response object 
for dict_item in proxyList:
	threading.Thread(target=g).start()

print(r.status_code, r.text)
time1 = time.perf_counter();
timetoprocess = str(time1-time0)
print("the sniper shot (2/2), it took " + timetoprocess + " seconds to send the requests!") 
# program has successfully executed. go check your account!