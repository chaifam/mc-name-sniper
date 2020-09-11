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

	def login(self):
		self.user = MojangUser(self.email, self.password)


def main():
	emails = config["email"]
	passwords = config["password"]
	accounts = list()
	for i in emails:
		new_account = account(i, passwords)
		accounts.append(new_account)

	with concurrent.futures.ThreadPoolExecutor() as executor:
		for account in accounts:
			executor.submit(account.login)
			print(f"Logging in on {accont.user}.")

if __name__ == '__main__':
	main()


