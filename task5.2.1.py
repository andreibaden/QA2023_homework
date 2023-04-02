# Task5.2 "Number"
#
# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 27.02.2023

def sum_arithmetic_pr(number):
    num_1 = number // 1000
    num_2 = number // 100 % 10
    num_3 = number // 10 % 10
    num_4 = number % 10
    sum_arithmetic = (num_1 + num_2 + num_3 + num_4) / 4
    return sum_arithmetic


def sum_geometric_pr(number):
    num_1 = number // 1000
    num_2 = number // 100 % 10
    num_3 = number // 10 % 10
    num_4 = number % 10
    sum_geometric = pow(num_1 * num_2 * num_3 * num_4, 1 / 4)
    return sum_geometric

def main():
    number = int(input("Please,input a four digit number: "))
    sum_arithmetic = sum_arithmetic_pr(number)
    sum_geometric = sum_geometric_pr(number)

    msg = f"\nArithmetic progression = {sum_arithmetic} \nGeometric progression = {sum_geometric}"

    print(msg)

main()
