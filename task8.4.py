# Task8.4 "Interval"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def interval(a, b, c, d, e):
    result = (a <= e < b) or (c < e <= d)
    return result


def english_UI(result, num):
    return f"The number {num} is included in the given \
interval!" if result else f"The number {num} is not \
included in the given interval!"


def main():
    a = int(input("Input your interval number #1: "))
    b = int(input("Input your interval number #2: "))
    c = int(input("Input your interval number #3: "))
    d = int(input("Input your interval number #4: "))
    e = int(input("Input your number: "))
    msg = interval(a, b, c, d, e)
    result = english_UI(msg, e)
    print(msg)
    print(result)


main()


def testing():
    result = "-9, -1, 1, 7, 3 --> " + str(interval\
    (-9, -1, 1, 7, 3) == True)
    result += "\n -9, -2, 5, 7, -9 --> " + str(interval\
    (-9, -2, 5, 7, -9) == True)
    result += "\n -1, 6, 4, 9, 9 --> " + str(interval\
    (-1, 6, 4, 9, 9) == True)
    result += "\n -9, -8, -7, -2, -1 --> " + str(interval\
    (-9, -8, -7, -2, -1) == False)
    print(result)


testing()
