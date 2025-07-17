#!/usr/bin/env python3
import os
import time as tm

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

cart = []
total = 0.0

nbr_products = int(input("How many products are you buying today?").strip())

print("Please, informe the name of the product followed by it's price\n[eg.: rice 3.50]")
for product in range(nbr_products):
	product_name = input(">>> ").strip().replace(",", ".")

	space_i = product_name.rfind(" ")

	item = product_name[:space_i]
	product_price = float(product_name[space_i + 1:])

	cart.append((item, product_price))
	total += product_price

tm.sleep(2)
clear()
print("This is your shopping cart:\n---------------------------")
for prod_nm, price in cart:
	print(f"{prod_nm}: R$" "{:.2f}".format(price))
print("---------------------------\nTotal: R$" "{:.2f}".format(total))