# Task12.5 "Mirror_number"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 08.04.2023

def check_mirror(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    for i in range(len(ls) // 2):
        if ls[i] != ls[len(ls) - 1 - i]:
            return False

    return True


def test():
    print(check_mirror([1, 2, 3, 2, 1]))
    print(check_mirror([-1, 2, -3, 2, -1]))
    print(check_mirror([9, 9, 3, 2, 1]))


if __name__ == "__main__":
    test()
