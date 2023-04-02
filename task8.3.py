# Task8.3 "Maximum number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def max_num(a, b):
    return a if a > b else b


def main():
    a = float(input("Input your number #1: "))
    b = float(input("Input your number #2: "))
    msg = max_num(a, b)
    print(f"The maximum number is: {msg}!")


main()


def testing():
    result = " 3, 5 --> 5  " + str(max_num(3, 5) == 5)
    result += "\n -7, 7 --> 7  " + str(max_num(-7, 7) == 7)
    print(result)


testing()
