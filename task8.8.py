# Task8.8 "Maximum number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 19.03.2023


def max_num(a, b, c, d):
    num1 = a if a > b else b
    num2 = c if c > d else d
    max_n = num1 if num1 > num2 else num2
    return max_n


def main():
    a = int(input("Input your number №1: "))
    b = int(input("Input your number №2: "))
    c = int(input("Input your number №3: "))
    d = int(input("Input your number №4: "))
    msg = max_num(a, b, c, d)
    print(f"The max number is {msg}!")


main()


def testing():
    result = "Your numbers are: 2, 0, -7, 9 --> 9 _" + \
             str(max_num(2, 0, -7, 9) == 9)
    result += "\nYour numbers are: 1, -5, 77, 6 -- 77 _>" + \
              str(max_num(1, -5, 77, 6) == 77)
    print(result)


testing()
