# Task8.1 "Even number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def even_or_odd(number):
    result = number % 2 == 0
    return f"Number is even" if result else "Number is odd"


def main():
    number = int(input("Input your integer number: "))
    msg = even_or_odd(number)
    print(msg)


main()


def testing():
    result = " 2 --> " + str(even_or_odd(2) == "Number is even")
    result += "\n 1 --> " + str(even_or_odd(1) == "Number is odd")
    result += "\n -31 --> " + str(even_or_odd(-31) == "Number is odd")
    result += "\n -56 --> " + str(even_or_odd(-56) == "Number is even")
    print(result)


testing()
