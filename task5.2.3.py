# Task5.2 "Number"
#
# Version: 3.0
# Author: Nedaboi Andrei_QA2023
# Date: 27.02.2023


def sum_digits(number):
    sum_dig = number % 10
    sum_dig += number % 100 // 10
    sum_dig += number % 1000 // 100
    sum_dig += number // 1000
    return sum_dig

def sum_arithmetic_pr(number):
    number = abs(number)
    if number >= 10000 or number <= 999:
        return "Error!"
    else:
        sum_digits(number)
        sum_arithmetic = round((sum_digits / 4), 1)
        return sum_arithmetic


def sum_geometric_pr(number):
    number = abs(number)
    if number >= 10000 or number <= 999:
        return "Error!"
    else:
        multipl_digits = number % 10
        multipl_digits *= number % 100 // 10
        multipl_digits *= number % 1000 // 100
        multipl_digits *= number // 1000
        sum_geometric = round(pow(multipl_digits, 1 / 4), 1)
        return sum_geometric


def main():
    number = int(input("Please,input a four digit number: "))
    sum_arithmetic = sum_arithmetic_pr(number)
    sum_geometric = sum_geometric_pr(number)
    msg = f"\nArithmetic progression = {sum_arithmetic} \nGeometric progression = {sum_geometric}"
    print(msg)


main()


def testing():
    result = " 0 --> " + str(sum_arithmetic_pr(0) == "Error!")
    result += "\n0 --> " + str(sum_geometric_pr(0) == "Error!")
    result += "\n-999 --> " + str(sum_arithmetic_pr(-999) == "Error!")
    result += "\n-999 --> " + str(sum_geometric_pr(-999) == "Error!")
    result += "\n2222 --> " + str(sum_arithmetic_pr(2222) == 2.0)
    result += "\n2222 --> " + str(sum_geometric_pr(2222) == 2.0)
    result += "\n-5555 --> " + str(sum_arithmetic_pr(-5555) == 5.0)
    result += "\n-5555 --> " + str(sum_geometric_pr(-5555) == 5.0)
    result += "\n10000 --> " + str(sum_arithmetic_pr(10000) == "Error!")
    result += "\n10000 --> " + str(sum_geometric_pr(10000) == "Error!")
    result += "\n10001 --> " + str(sum_arithmetic_pr(10001) == "Error!")
    result += "\n10001 --> " + str(sum_geometric_pr(10001) == "Error!")

    print(result)


testing()
