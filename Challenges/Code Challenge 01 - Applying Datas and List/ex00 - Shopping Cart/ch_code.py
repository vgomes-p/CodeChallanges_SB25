#!/usr/bin/env python3
cart = []
total = 0.0

nbr_products = int(input().strip())

for product in range(nbr_products):
	product_name = input().strip()

	space_i = product_name.rfind(" ")

	item = product_name[:space_i]
	product_price = float(product_name[space_i + 1:])

	cart.append((item, product_price))
	total += product_price

for prod_nm, price in cart:
	print(f"{prod_nm}: R$" "{:.2f}".format(price))
print("Total: R$" "{:.2f}".format(total))