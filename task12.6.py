# Task12.6 "Same/Different numbers"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 08.04.2023

def same_num(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    for i in range(len(ls) - 1):
        if ls[i] != ls[i + 1]:
            return False

    return True


# first = ls[0]
#
#    for item in ls:
#        if first != item:
#            return False

def test():
    print(same_num([2, 2, 2]))
    print(same_num([-3, 3, 3]))
    print(same_num([12, 15, 12]))


if __name__ == "__main__":
    test()
