# Task5.3 "Number reverse"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 22.02.2023

number = int(input("Please,input a four digit number > 0: "))

num_1 = number // 1000
num_2 = number // 100 % 10
num_3 = number // 10 % 10
num_4 = number % 10

number_rev = num_4 * 1000 + num_3 * 100 + num_2 * 10 + num_1

print(f"\n Your number is {number}. \n Number reverse is {number_rev}.")