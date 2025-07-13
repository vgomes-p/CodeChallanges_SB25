#!/usr/bin/env python3
import os
import time as tm

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_number(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

discounts = {
	"DESC10": 0.10,
	"DESC20": 0.20,
	"NO_DESC": 0.00
}

sigexit = 0
used_cupons = []

clear()
while sigexit != 1:
	price = input("Please enter the price of the product you are interested in!\n>>> $").strip()
	if price:
		if is_valid_number(price):
			cupom = input("If you do have a cupom, enter it. {All cupons are one time use}\n>>> ").strip()
			if cupom in used_cupons:
				clear()
				print("This cupon was already used!")
				tm.sleep(3)
				clear()
				continue
			else:
				if cupom in discounts:
					discount = discounts[cupom]
					final_price = price - (price * discount)
					formated_final_price = "{:.2f}".format(final_price)
					print(f"The final price is: ${formated_final_price}")
					tm.sleep(1)
				else:
					clear()
					print("Cupom not found!")
					tm.sleep(3)
					clear
					continue
			used_cupons.append(cupom)
			# print(f"DEBUG: the cupons used are {used_cupons}")
		else:
			clear()
			print("Please, enter only numbers")
			tm.sleep(3)
			clear()
			continue
		tm.sleep(5)
		clear()
		new_product = input("Do you want to check the discount for any other product?\n[y for yes, n for no]\n>>> ").lower()
		if new_product == "y":
			print("Please, wait a moment!")
			tm.sleep(4)
			clear()
			continue
		else:
			sigexit = 1
	else:
		clear()
		print("Empty entries are not acceptable!")
		tm.sleep(4)
		clear()
		continue
clear()
print("Program finished!")