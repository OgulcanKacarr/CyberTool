from colorama import Fore, Back, Style
from termcolor import colored, cprint
import subprocess
import colorama
import requests
import time
import wget
import os

colorama.init()
os.system("clear")
os.system("cls")

def sendmessage(message):
	subprocess.Popen(['notify-send', message])
	return
				
def startAttack(wordlist,cookie,target):
	file = open(wordlist,"r")
	content = file.read()
	file.close()

	try:
		for i in content.split("\n"):
			link = target + str(i)
			sonuc = requests.get(url=link,headers=cookie)	#burpdan cookie al dene auth için
			if "200" in str(sonuc.status_code):
				print(Fore.BLUE)
				print("Found >>",i)
				print(Fore.GREEN)
				print(url + i)
				print(Fore.GREEN)
				print("____________")
			else:
				print(Fore.RED)
				print("no --X",i)	
	except FileNotFoundError: 
		print("Wordlist is not found")


def searcXSS(wordlist,target,cookie):
	file = open(wordlist,"r")
	content = file.read()
	file.close()

	for payload in content:
		print(payload)
		url = target + str(payload)
		result = requests.get(url=url,header=cookie)
		if str(payload) in str(result.content):
			print("Muhtemelen XSS var >>>", str(payload))			


print(Fore.GREEN)
print("""



	[1] - Fuzzing
	[2] - Search XSS



	""")


print(Fore.RED)


userInput = int(input("Please select a options: "))
if userInput == 1:
	try:
		print(Fore.GREEN)
		cookie = input("Please enter cookie (get Burp): ")
		print(Fore.BLUE)
		url = input("Please enter target url (Http://...): ")
		print(Fore.RED)
		wordlist = input("Please enter wordlist: ")
		os.system("clear")
		print(Fore.GREEN)
		print("[+] Cookie >>> " + str(cookie))
		print("[+] Target >>> " + str(url))
		print("[+] Wordlist >>> " + str(wordlist))
		startAttack(wordlist,cookie,url)
	except TypeError:
		print(Fore.RED)
		print("Enter wordlist ! (-w <wordlist.txt>)")

elif userInput == 2:
		try:
			print(Fore.GREEN)
			cookie = input("Please enter cookie (get Burp): ")
			print(Fore.BLUE)
			url = input("Please enter target url (Http://...): ")
			print(Fore.RED)
			wordlist = input("Please enter xss command wordlist: ")
			print(Fore.BLUE)
			print("""

					your command list in xss command:
					ör:// <h1> alert </h1>

				""")
			time.sleep(3)
			os.system("clear")
			print(Fore.GREEN)
			print("[+] Cookie >>> " + str(cookie))
			print("[+] Target >>> " + str(url))
			print("[+] Wordlist >>> " + str(wordlist))
			searcXSS(wordlist,url,cookie)
		except:
			print(Fore.RED)
			exit()
			










