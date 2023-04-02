# Task3.1 "First digit of a three-digit number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 13.02.2023

n_num = int(input("Enter a three-digit number: "))

if n_num >= 100 and n_num <= 999:
    print("First digit of a three-digit number = ", n_num // 100)
else:
    print("Be careful!!! Enter a valid three-digit number!!!")
