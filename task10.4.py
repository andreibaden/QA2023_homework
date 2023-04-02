# Task10.4 "The bank deposit"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def deposit(num, p):
    num_m = 1

    if num < 0 or p < 0:
        return "Error! Input the correct numbers!"

    num_f = num * (1 + p / 100)
    while num_f < (num * 2):
        num_f = num_f * (1 + p / 100)
        num_m += 1
    return f"You can receive your deposit of {num_f} rubles in {num_m} months!"


def main():
    dep_start = float(input("Input your start deposit > 0: "))
    percent = float(input("Input your deposit percentage > 0: "))
    result = deposit(dep_start, percent)
    print(result)


main()

def testing():
    result = " 300, 15 --> " + str(deposit(300, 15) == "You can receive your deposit of 603.4071562499998 rubles in 5 months!")
    result += "\n23, - 100 --> Error! Input the correct numbers! _" + \
              str(deposit(23, - 100) == "Error! Input the correct numbers!")
    result += "\n-6, 5 --> Error! Input the correct numbers! _" + \
              str(deposit(-6, 5) == "Error! Input the correct numbers!")
    print(result)


testing()
