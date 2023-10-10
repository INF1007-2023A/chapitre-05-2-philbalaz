#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	prix = 0
	for i in range(0, len(data)):
		prix += data[i][1]*data[i][2]
	taxes = prix*0.15
	total = prix+taxes
	return f"\n{name} \nSOUS TOTAL\t{prix: >10.2f}$ \nTAXES\t\t{taxes: >10.2f}$ \nTOTAL\t\t{total: >10.2f}"


def format_number(number, num_decimal_digits):
	decimal_part = abs(number) % 1.0
	entier = int(abs(number))

	decimal_str = f"{decimal_part :.{num_decimal_digits}f}"[1:]

	# formatter entier
	entier_str=""
	compteur = 1
	for i in str(entier):
		if compteur%3==0:
			entier_str+=" "
		entier_str += i
		compteur+=1
	
	return ("-" if number<0 else "") + entier_str+decimal_str


def get_triangle(num_rows):
	string=""
	i=0
	while i <= num_rows+1:
		ligne = "+"
		if i == 0 or i == num_rows+1:
			ligne += 2*num_rows*"+"
		else:
			A = ((num_rows-i)*" "+(i-1)*"A")
			ligne += A+"A"+A[::-1]+"+"
		string+=f"\n{ligne}"
		i+=1

	return string


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
