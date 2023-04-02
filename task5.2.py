# Task5.2 "Number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 22.02.2023

number = int(input("Please,input a four digit number: "))

num_1 = number // 1000
num_2 = number // 100 % 10
num_3 = number // 10 % 10
num_4 = number % 10

# sum_arithmetic_pr = round(((num_1 + num_2 + num_3 + num_4) / 4), 2)
# sum_geometric_pr = round((pow(num_1 * num_2 * num_3 * num_4, 1. / 4)), 2)

sum_arithmetic_pr = (num_1 + num_2 + num_3 + num_4) / 4
sum_geometric_pr = pow(num_1 * num_2 * num_3 * num_4, 1/4)

print(f"\n Arithmetic progression = {sum_arithmetic_pr} \ngeometric progression = {sum_geometric_pr}.")
