# Task3.4 "Even number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.02.2023

number = int(input("Please,input your number > 0: "))

if number > 0:
    if number % 2 == 0:
        e_number = number + 2
    else:
        e_number = number + 1
    print("Next even number is ", e_number)
else:
    print("Error! Input a correct number!")


