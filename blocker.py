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

	def __init__ (self, email, password):
		self.email = email
		self.password = password
		self.user = MojangUser(self.email, self.password, maximum_pool_size = 3)

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
	

