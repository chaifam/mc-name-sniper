import time
import os
import json
import random, string
import concurrent.futures
from colorama import init
from termcolor import colored
from mojang import MojangAPI, MojangUser

#x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
#y = x + "@gmail.com"
#print(y)

init()

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)
with open("config.json", "r") as f:
	config = json.load(f)

class account:
	newname = input("Input name to be blocked: \n")
	user = None

	def __init__ (self, email, password):
		self.email = email
		self.password = password

	# def login(self):
	# 	user = MojangUser(self.email, self.password)
	# 	return user

	def block(self):
		drop_timestamp = MojangAPI.get_drop_timestamp(self.newname)
		user = MojangUser(self.email, self.password)
		if not drop_timestamp:
			print(colored(f"{self.newname} is not dropping", "cyan"))
		else:
			seconds = drop_timestamp - time.time()
			time.sleep(seconds)
			
		if user.block_username(self.newname):
			print(f"Blocked the username {self.newname}")
			time.sleep(35)
			if user.block_username({self.newname}):
				print("Success!")
			else:
				print("False positive :(")


emails = config["email"]
passwords = config["password"]

accounts = list()
for i in emails:
	accounts.append(account(i, passwords))

with concurrent.futures.ThreadPoolExecutor() as executor:
	for account in accounts:
		#executor.submit(obj.login)
		print(f"Logging in on {account.email} {account.password}.")
		for _ in range(3):
			executor.submit(account.block)