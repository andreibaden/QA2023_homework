# Task8.6 "Number of positive numbers"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def amount_num(a, b, c, d):
    sum_n = 0
    a = [a, b, c, d]
    for i in (range(0, 4)):
        if a[i] > 0:
            sum_n += 1

    return sum_n


def main():
    a = int(input("Input your number #1: "))
    b = int(input("Input your number #2: "))
    c = int(input("Input your number #3: "))
    d = int(input("Input your number #4: "))
    msg = amount_num(a, b, c, d)
    print(f"Number of positive numbers is {msg}!")


main()


def testing():
    result = "2, 1, 3, 4 --> " + str(amount_num(2, 1, 3, 4) == 4)
    result += "\n-5, 5, 4, 8 --> " + str(amount_num(-5, 5, 4, 8) == 3)
    result += "\n-1, 0, -10, 8 --> " + str(amount_num(-1, 0, -10, 8) == 1)
    print(result)


testing()
