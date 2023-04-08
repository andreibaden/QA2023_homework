# Task12.6 "Even/Odd number"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 08.04.2023

def even_num(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    even_num = 0
    i = 0
    while (len(ls) - 1) >= i:
        if ls[i] % 2 == 0:
            even_num += 1
        i += 1
    return even_num

def odd_num(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    odd_num = 0
    i = 0
    while (len(ls) - 1) >= i:
        if not ls[i] % 2 == 0:
            odd_num += 1
        i += 1
    return odd_num

def test():
    result = (f" The even numbers from list = [2, 24, 33, 77] is \
{even_num([2, 33, 0, 7, 8])}.")
    result  += ( f"\n The even numbers from list = [-3, -1, -3, 0] is \
{even_num([-2, -16, -34, -4])}.")
    result  += (f"\n The even numbers from list = [-3, -1, -3, 0] is \
{even_num([11, 15, 7])}.")
    result += (f"\n The odd numbers from list = [2, 24, 33, 77] is \
{odd_num([2, 31, 0, 77, 45])}.")
    result += (f"\n The odd numbers from list = [2, 24, 33, 77] is \
{odd_num([-1, -4, -3, -77, -7, -7])}.")
    result += (f"\n The odd numbers from list = [2, 24, 33, 77] is \
{odd_num([2, 24, 8])}.")
    print(result)

if __name__ == "__main__":
    test()
