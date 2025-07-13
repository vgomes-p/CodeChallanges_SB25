#!/usr/bin/env python3

"NOTE: take the string from the inputs to validate on DIO platform"

discounts = {
	"DESCONTO10": 0.10,
	"DESCONTO20": 0.20,		"SEM_DESCONTO": 0.00
}

price = float(input("Please enter the price of the product you are interested in!\n>>> $").strip())
cupom = input("If you do have a cupom, enter it.\n>>> ").strip()

if cupom in discounts:
	discount = discounts[cupom]
	final_price = price - (price * discount)
	formated_final_price = "{:.2f}".format(final_price)
	print(f"The final price is: ${formated_final_price}")
else:
	print("Cupom not found!")

### VERSION ACCEPCTED BY THE DIO PLATFORM:
# discounts = {
# 	"DESCONTO10": 0.10,
# 	"DESCONTO20": 0.20,		"SEM_DESCONTO": 0.00
# }

# price = float(input().strip())
# cupom = input().strip()

# if cupom in discounts:
# 	discount = discounts[cupom]
# 	final_price = price - (price * discount)
# 	formated_final_price = "{:.2f}".format(final_price)
# 	print(formated_final_price)
# else:
# 	print("Cupom not found!")