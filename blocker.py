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

	def __init__ (self, email, password):
		self.email = email
		self.password = password

	def login(self):
		user = MojangUser(self.email, self.password)
		return user


def block():	
	drop_timestamp = MojangAPI.get_drop_timestamp(newname)
	if not drop_timestamp:
		print(colored(f"{newname} is not dropping", "cyan"))
	else:
		seconds = drop_timestamp - time.time()
		print(colored(f"{newname} drops in {seconds} seconds", "cyan"))
		
	if user.block_username(newname, seconds):
		print(f"Blocked the username {newname}")
		time.sleep(35)
		if user.block_username({newname}):
			print("Success!")
		else:
			print("False positive :(")

newname = input("Input name to be blocked: \n")
emails = config["email"]
passwords = config["password"]

accounts = list()
for i in emails:
	accounts.append(account(i, passwords))

for obj in accounts:
	print(obj.login())
