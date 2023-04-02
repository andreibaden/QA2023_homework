# Task3.2 "Last digit of a natural number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 13.02.2023

num = int(input("Enter a natural number: "))

if num >= 10:
    print("Last digit of a natural number = ", num % 10)
else:
    print("Last digit of a natural number = ", num)
