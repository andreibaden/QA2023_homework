# Task12.4 "Ordered Values"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 07.04.2023

def check_soft_asc(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    for i in range(len(ls) - 1):
        if not ls[i] < ls[i + 1]:
            return False

    return True


def check_soft_desc(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    for i in range(len(ls) - 1):
        if not ls[i] > ls[i + 1]:
            return False

    return True

def check(ls):
    return check_soft_desc(ls) or check_soft_asc(ls)


def test():
    print(check([2, 3, 4, 5, 6]))
    print(check([-6, -5, -4, -3]))
    print(check([7, 5, 4, 2, 1]))
    print(check([5, 3, 4, 5, 6]))
    print(check([4, 4, 5, 6]))
    print(check([-4, 0, 0, -4]))


if __name__ == "__main__":
    test()



