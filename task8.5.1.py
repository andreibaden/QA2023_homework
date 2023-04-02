# Task8.5 "Sum of numbers"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 18.03.2023

def sum_num(m, q):
    sum_n = 0
    for i in (range(0, q)):
        if m[i] > 0:
            sum_n += 1

    return sum_n


def main():
    q = int(input("Input amount of numbers: "))
    m = [0] * q
    for i in range(0, q):
        m[i] = int(input("Input your number: "))
    msg = sum_num(m, q)
    print(f"Sum of positive numbers is {msg}!")


main()


def testing():
    a1 = [2, 1, 3, 4]
    q1 = 4
    a2 = [-3, 6, 0]
    q2 = 3
    result = "a1[2, 1, 3, 4] --> 4 _" + str(sum_num(a1, q1) == 4)
    result += "\na2[-3, 6, 0] --> 1 _" + str(sum_num(a2, q2) == 1)
    print(result)


testing()
