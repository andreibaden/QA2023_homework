# Task12.3 "Change the last and first number in the list"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 04.04.2023


def change_number(ls):
    max_num = max(ls)
    max_ind = 0
    for i in range(0, len(ls)):
        if ls[i] == max_num:
            max_ind = i
            break

    min_num = min(ls)
    min_ind = 0
    for i in range(0, len(ls)):
        if ls[i] == min_num:
            min_ind = i
            break

    n = ls[min_ind]
    ls[min_ind] = ls[max_ind]
    ls[max_ind] = n
    return ls


def testing():
    result = " test1: [9, 7, 1, 5] --> [1, 7, 9, 5] _ " + str(change_number([9, 7, 1, 5]) == [1, 7, 9, 5])
    result += "\n test2: [6, 3, 2, 8, 8] --> [6, 3, 8, 2, 8] _ " + \
              str(change_number([6, 3, 2, 8, 8]) == [6, 3, 8, 2, 8])
    result += "\n test3: [-5, -5, 0, 0, -3, 4, 4] --> [4, -5, 0, 0, -3, -5, 4] _ " + \
              str(change_number([-5, -5, 0, 0, -3, 4, 4]) == [4, -5, 0, 0, -3, -5, 4])
    print(result)


if __name__ == "__main__":
    testing()
