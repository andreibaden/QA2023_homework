# Task12.1 "Extreme number"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 04.04.2023


def max_number(ls):
    return max(ls)


def min_number(ls):
    return min(ls)


def mean_number(ls):
    mean_num = sum(ls) / len(ls)
    return mean_num


ls = [6, 3, 8, 77, 9, 12, -10, -28]
print(f" Maximum number is {max_number(ls)}! \
\n Minimum number is {min_number(ls)}! \
\n Arithmetic mean number is {mean_number(ls)}!")


def testing():
    tst = [-1, 3, 6, 88, 9, 2, -10, -9]
    result = "\n Testing_ Max number (tst) = 88 _ " + str(max_number(tst) == 88)
    result += "\n Testing_ Min number (tst) = -10 _ " + str(min_number(tst) == -10)
    result += "\n Testing_ Mean_number (tst) = 11.0 _ " + str(mean_number(tst) == 11.0)
    print(result)


if __name__ == "__main__":
    testing()
