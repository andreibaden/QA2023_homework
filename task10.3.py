# Task10.3 "The same number"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def same_num(number, num):
    q = 0

    if number < 0 or 10 < num or num < - 1:
        return "Error! Input the correct numbers!"

    while number > 0:
        last_digit = number % 10
        if last_digit == num:
            q += 1
        number //= 10
    return q


def main():
    number = int(input("Input your number > 0: "))
    num = int(input("Input your number from 0 to 9: "))
    msg = same_num(number, num)
    print(msg)


main()


def testing():
    result = " 345, 4 --> 1 _" + str(same_num(345, 4) == 1)
    result += "\n 7321, 5 --> 0 _" + str(same_num(7321, 5) == 0)
    result += "\n -321, 3 --> Error! Input the correct numbers!  _" + \
              str(same_num(-321, 3) == "Error! Input the correct numbers!")
    result += "\n 3567, -3 --> Error! Input the correct numbers!  _" + \
              str(same_num(3567, -3) == "Error! Input the correct numbers!")
    result += "\n 1111, 11 --> Error! Input the correct numbers!  _" + \
              str(same_num(3567, 11) == "Error! Input the correct numbers!")
    print(result)


testing()
