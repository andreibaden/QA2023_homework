# Task8.6 "Number (amount) of positive numbers"
#
# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def sum_num(a, q):
    sum_n = 0
    for k in range(0, q):
        if a[k] > 0:
            sum_n += 1

    return sum_n


def main():
    q = int(input("Input amount of numbers: "))
    a = [0] * q
    for i in range(0, q):
        a[i] = int(input("Input your number: "))
    msg = sum_num(a, q)
    print(f"Number (amount) of positive numbers is {msg}!")


main()

def testing():
    a1 = [2, 1, 3, 4]
    q1 = 4
    a2 = [-3, -6]
    q2 = 2
    a3 = [-1, 9, -2, 7, 5, 0]
    q3 = 6
    result = "a1[2, 1, 3, 4] --> 4 _ " + str(sum_num(a1, q1) == 4)
    result += "\na2[-3, -6] --> 0 _" + str(sum_num(a2, q2) == 0)
    result += "\na3[-1, 9, -2, 7, 5, 0] --> 3 _" + str(sum_num(a3, q3) == 3)
    print(result)


testing()
