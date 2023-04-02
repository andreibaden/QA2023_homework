# Task8.5 "Sum of numbers"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def sum_num(a, b, c, d):
    sum_n = 0
    if a > 0:
        sum_n += a
    if b > 0:
        sum_n += b
    if c > 0:
        sum_n += c
    if d > 0:
        sum_n += d
    return sum_n


def main():
    a = int(input("Input your number #1: "))
    b = int(input("Input your number #2: "))
    c = int(input("Input your number #3: "))
    d = int(input("Input your number #4: "))
    msg = sum_num(a, b, c, d)
    print(msg)


main()


def testing():
    result = "2, 1, 3, 4 --> " + str(sum_num(2, 1, 3, 4) == 10)
    result += "\n-5, 5, -4, 8 --> " + str(sum_num(-5, 5, -4, 8) == 13)
    print(result)


testing()
