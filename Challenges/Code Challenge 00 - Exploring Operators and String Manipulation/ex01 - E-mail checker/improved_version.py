#!/usr/bin/env python3
import os
import time as tm

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def error_message(message, delay=3):
	clear()
	print(message)
	tm.sleep(delay)

domains = ["gmail.com", "outlook.com"]
registered_emails = []

sigexit = 0

clear()
while sigexit != 1:
	email = input("Welcome to the email validator, please enter the address you want to validate\n>>> ").strip()
	if email:
		if " " in email:
			error_message(message="Invalid email, spaces are not acceptable!")
		else:
			if "@" in email:
				if email.startswith("@") or email.endswith("@"):
					error_message(message="Invalid email, '@' cannot be at the beginning or end!")
				else:
					if email.count("@") == 1:
						email_check = email.split("@")
						# print(f"DEBUG: {email} after split {email_check}")
						if email_check[1] in domains:
							if email in registered_emails:
								clear()
								print("This email is valid and is registered in our system!")
								tm.sleep(2)
							else:
								registered_emails.append(email)
								# print(f"DEBUG: emails registered: {registered_emails}")
								clear()
								print("This email is valid and is not registered in our system!")
								tm.sleep(2)
						else:
							error_message(message=f"Invalid email, the domain '{email_check[1]}' is not acceptable!")
					else:
						error_message(message="Invalid email, email address cannot contain more than one '@'!")
			else:
				error_message(message="Invalid email, it does not contains '@'!")
	else:
		error_message(message="Empty entries cannot be checked!", delay=4)
		clear()
		continue
	print("Do you want to check another email?\n[y for yes, n for no]")
	while True:
		nw_check = input(">>> ").lower()
		if nw_check == 'y':
			print("Please, wait a moment...")
			tm.sleep(1.5)
			clear()
			break
		elif nw_check == 'n':
			sigexit = 1
			break
		else:
			error_message(message="Please, answer as oriented!\n[y for yes, n for no]", delay=.5)
			continue
clear()
print("Program finished!")