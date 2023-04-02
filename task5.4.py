# Task5.4 "Century number"
#
# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 28.02.2023


def century_n(number):
    if number == 0:
        return "Error! Input correct number!"

    number_sign = number
    number = abs(number)
    if 100 > number > 0:
        century_num = 1
    elif number % 100 == 0:
        century_num = number // 100
    else:
        century_num = number // 100 + 1

    century_num *= 1 if number_sign > 0 else -1
    return century_num


def main():
    number = int(input("Please,input year: "))
    msg = century_n(number)
    print(f"\n Your year number is {number}.\n Your century is {msg}!")


main()


def testing():
    result = " 0 --> " + str(century_n(0) == "Error! Input correct number!")
    result += "\n -99 --> " + str(century_n(-99) == -1)
    result += "\n -1456 --> " + str(century_n(-1456) == -15)
    result += "\n 185 --> " + str(century_n(185) == 2)
    result += "\n 879 --> " + str(century_n(879) == 9)

    print(result)


testing()
