# Task7.1 "Time of the year"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 01.03.2023

def time_of_year(number):
    if number > 12 or number <= 0:
        return "Error! Input correct number!"

    if number == 12 or number == 1 or number == 2:
        time = "winter"
    elif number >= 3 and number <= 5:
        time = "spring"
    elif number >= 6 and number <= 8:
        time = "summer"
    elif number >= 9 and number <= 11:
        time = "autumn"
    return time


def main():
    number = int(input("Please,input your number month: "))
    msg = time_of_year(number)
    print(f"\n Your number month is {number}.\n Your time of the year is {msg}!")


main()


def testing():
    result = "-1 --> " + str(time_of_year(-1) == "Error! Input correct number!")
    result += "\n 12 --> " + str(time_of_year(12) == "winter")
    result += "\n 3 --> " + str(time_of_year(3) == "spring")
    result += "\n 8 --> " + str(time_of_year(8) == "summer")
    result += "\n 10 --> " + str(time_of_year(10) == "autumn")
    result += "\n 13 --> " + str(time_of_year(13) == "Error! Input correct number!")
    print(result)


testing()
