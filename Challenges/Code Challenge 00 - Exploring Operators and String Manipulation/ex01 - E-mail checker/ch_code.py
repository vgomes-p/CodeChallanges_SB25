#!/usr/bin/env python3
"NOTE: take the string from the inputs to validate on DIO platform"

"OPTION 1:"
email = input("Email: ").strip() #take the string from the input to validate on DIO platform

if " " in email:
	print("Invalid E-mail")
else:
	if email.endswith("@") or email.startswith("@"):
		print("Invalid E-mail")
	else:
		if email.endswith("@gmail.com") or email.endswith("@outlook.com"):
				print("Valid E-mail")
		else:
				print("Invalid E-mail")


# "OPTION 2:"
# domains = ["gmail.com", "outlook.com"]

# email = input("Email: ").strip()

# if " " in email:
# 	print("Invalid E-mail")
# else:
# 	if "@" in email:
# 		if email.startswith("@") or email.endswith("@"):
# 			print("Invalid E-mail")
# 		else:
# 			email_check = email.split("@")
# 			# print(f"DEBUG: {email} after split {email_check}")
# 			if email_check[1] in domains:
# 				print("Valid E-mail")
# 			else:
# 				print("Invalid E-mail")
# 	else:
# 		print("Invalid E-mail")