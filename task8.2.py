# Task8.2 "The absolute value of a number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def absolute_value(number):
    return number if number > 0 else number * (-1)


def main():
    number = int(input("Input your number: "))
    msg = absolute_value(number)
    print(f"The absolute value of a number {number} --> {msg}!")


main()


def testing():
    result = " 3 --> " + str(absolute_value(3) == 3)
    result += "\n -7 -->" + str(absolute_value(-7) == 7)
    print(result)


testing()
