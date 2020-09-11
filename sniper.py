import time
import os
import json
from colorama import init
from termcolor import colored
from mojang import MojangAPI, MojangUser

init()

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)
with open("config.json", "r") as f:
	config = json.load(f)

class profile:
	def __init__ (self, email, password):
		self.email = email
		self.password = password

numAccounts = len(config["emails"])

for e in range(numAccounts):
	c = profile(config["emails"][e], config["passwords"][e])
	print(c.email, c.password)

user = MojangUser(c.email, c.password)
newname = input("Input name to be blocked: \n")
drop_timestamp = MojangAPI.get_drop_timestamp(newname)
if not drop_timestamp:
	print(colored(f"{newname} is not dropping", "cyan"))
else:
	seconds = drop_timestamp - time.time()
	print(colored(f"{newname} drops in {seconds} seconds", "cyan"))
