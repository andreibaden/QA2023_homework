# Task8.7 "The beautiful number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 19.03.2023

def number(num):
    return 10000 > num > 999 and (num % 9 == 0 or num % 19 == 0)


def cool_num(num):
    return "YES" if number(num) else "NO"


def main():
    num = int(input("Input your number: "))
    msg = cool_num(num)
    print(msg)


main()


def testing():
    result = "1019 --> NO _" + str(cool_num(1019) == "NO")
    result += "\n7677 --> YES _" + str(cool_num(7677) == "YES")
    result += "\n19 --> NO _" + str(cool_num(19) == "NO")
    result += "\n99999 --> NO _" + str(cool_num(99999) == "NO")
    print(result)


testing()
