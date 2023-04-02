# Task3.5 "Sweet pies"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.02.2023

pie_price = float(input("Please,input a pie price: "))
quantity = int(input("Please,input the number of pies: "))

rub = int(pie_price)  # price for one pie in rubles
coin = int((pie_price - rub) * 100)  # price for one pie in coins

n_pie = pie_price * quantity  # price for "n" pies
n_rub = int(n_pie)  # price for "n" pies in rubles
n_coin = int((n_pie - n_rub) * 100)  # price for "n" pies in rubles

print("\n Сost of one pie = {} rubles and {} coins".format(rub, coin))
print("\n Сost of {} pies = {} rubles and {} coins".format(quantity, n_rub, n_coin))
