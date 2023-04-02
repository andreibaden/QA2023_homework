# Task10.1 "Number (amount) of numbers"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def amount_num(num):
    amount = 0

    if num <= 0:
        return "Error! Input your number > 0!"

    while num > 0:
        amount += 1
        num //= 10

    return amount


def main():
    number = int(input("Input your number > 0: "))
    msg = amount_num(number)
    print(f"Number (amount) of numbers is: {msg}!")


main()


def testing():
    result = " 234 --> 3  " + str(amount_num(234) == 3)
    result += "\n 678912345 --> 9  " + str(amount_num(678912345) == 9)
    print(result)


testing()
