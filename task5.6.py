# Task5.6 "Simmetrical number"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 01.03.2023

def digits(number):
    if number > 10000 or number < 1000:
        return "Error! Input correct number!"

    num_1 = number // 1000
    num_2 = number // 100 % 10
    num_3 = number // 10 % 10
    num_4 = number % 10
    result = "Yes" if num_1 == num_4 and num_2 == num_3 else "No"
    return result


def main():
    number = int(input("Please,input four digit number: "))
    msg = digits(number)
    print(f"\n Your number is {number}.\n Is your number simmetrical? {msg}!")


main()


def testing():
    result = "-9 --> " + str(digits(-9) == "Error! Input correct number!")
    result += "\n 66 --> " + str(digits(66) == "Error! Input correct number!")
    result += "\n 4554 --> " + str(digits(4554) == "Yes")
    result += "\n 2345 --> " + str(digits(2345) == "No")
    result += "\n 78789 --> " + str(digits(78789) == "Error! Input correct number!")
    print(result)


testing()
