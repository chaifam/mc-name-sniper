import time
import os
import json
import random, string
import concurrent.futures
from colorama import init
from termcolor import colored
from mojang import MojangAPI, MojangUser
from mojang.exceptions import SecurityAnswerError

#x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
#y = x + "@gmail.com"
#print(y)

init()

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)
with open("config.json", "r") as f:
	config = json.load(f)

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

class account:
	newname = input("Input name to be blocked: \n")

	def __init__ (self, email, password):
		self.email = email
		self.password = password
		self.user = MojangUser(self.email, self.password, maximum_pool_size = 3)
		if self.user.is_fully_authenticated:
			print("Authenticated, security challenges are not required.")
		else:
			print(self.user.security_challenges) 
			answers = ["riseAndSnipe", "riseAndSnipe", "riseAndSnipe"]
			try:
				self.user.answer_security_challenges(answers)
			except SecurityAnswerError:
				print("A security answer was answered incorrectly.")

	def block1(self):
		if self.user.block_username(self.newname):
			print(colored(f"Blocked the username {self.newname}", "cyan"))

			time.sleep(35)
			if user.block_username(self.newname):
				string = colored("Block confirmed", "green")
				return string
			else:
				string = colored("False positive :(", "magenta")
				return string

	def block(self):	
		with concurrent.futures.ThreadPoolExecutor() as executor:
			results = [executor.submit(self.block1()) for req in range(3)]
			for f in concurrent.futures.as_completed(results):
				print(f.result)


emails = config["email"]
passwords = config["password"]
accounts = list()
for i in emails:
	new_account = account(i, passwords)
	accounts.append(new_account)

for account in accounts:
	print(f"Logging in on {account.email} {account.password}.")
	account.block()
	

