# Task12.1 "Positive and negative numbers"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 04.04.2023

def pos_number(elem):
    pos_num = 0
    for i in range(0, len(elem)):
        if elem[i] > 0:
            pos_num += 1
    return pos_num


def neg_number(elem):
    neg_num = 0
    for i in range(0, len(elem)):
        if elem[i] < 0:
            neg_num += 1
    return neg_num


def zero_number(elem):
    zero_num = 0
    for i in range(0, len(elem)):
        if elem[i] == 0:
            zero_num += 1
    return zero_num


ls = [6, -3, 8, 77, 0, 12, -10, -28]
print(f" Positive number is {pos_number(ls)}! \
\n Negative number is {neg_number(ls)}! \
\n Zero number is {zero_number(ls)}!")

def testing():
    tst1 = [-1, 3, 0, 88, -9, 0, -10, 0]
    tst2 = [1, 3, 88, 9, 10, 9]
    tst3 = [-1, -3, -2, -210]
    result = " Testing_ Positive number (tst1) = 2 _ " + str(pos_number(tst1) == 2)
    result += "\n Testing_ Positive number (tst3) = 0 _ " + str(pos_number(tst3) == 0)
    result += "\n Testing_ Negative number (tst1) = 3 _ " + str(neg_number(tst1) == 3)
    result += "\n Testing_ Negative number (tst2) = 0 _ " + str(neg_number(tst2) == 0)
    result += "\n Testing_ Zero_number (tst1) = 3 _ " + str(zero_number(tst1) == 3)
    result += "\n Testing_ Zero_number (tst2) = 0 _ " + str(zero_number(tst2) == 0)
    print(result)

if __name__ == "__main__":
    testing()
