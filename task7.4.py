# Task7.4 "Day of the week"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 05.03.2023

def day_week(number):
    if number > 8 or number < 1:
        return "Error! Input correct number!"

    if number == 1:
        day_w = "Monday"
    elif number == 2:
        day_w = "Thursday"
    elif number == 3:
        day_w = "Wednesday"
    elif number == 4:
        day_w = "Thursday"
    elif number == 5:
        day_w = "Friday"
    elif number == 6:
        day_w = "Saturday"
    else:
        day_w = "Sunday"
    return day_w


def main():
    number = int(input("Please, input your number from 1 to 7: "))
    msg = day_week(number)
    print(f"\n Your number is {number}.\n Your day of the week is {msg}!")


main()


def testing():
    result = " -1 --> " + str(day_week(-1) == "Error! Input correct number!")
    result += "\n 1 --> " + str(day_week(1) == "Monday")
    result += "\n 4 --> " + str(day_week(4) == "Thursday")
    result += "\n 7 --> " + str(day_week(7) == "Sunday")
    result += "\n 9 --> " + str(day_week(9) == "Error! Input correct number!")
    print(result)


testing()
