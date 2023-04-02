# Task10.2 "Same numbers"

# Version: 2.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def same_num(num):
    if num <= 9:
        return "Error! Input your number >= 10!"

    while num > 9:
        last_digit = num % 10
        last2_digit = num % 100 // 10
        if last_digit != last2_digit:
            return False
        num //= 10
    return True


def main():
    number = int(input("Input your number >= 10: "))
    msg = "Error! Input your number >= 10!" if same_num(number) == \
    "Error! Input your number >= 10!" else ("YES" if same_num(number) == True else "NO")
    print(msg)


main()


def testing():
    result = " 222 --> True _" + str(same_num(222) == True)
    result += "\n 345 --> False _" + str(same_num(345) == False)
    result += "\n 9 --> Error! Input your number >= 10!  _" + \
              str(same_num(9) == "Error! Input your number >= 10!")
    result += "\n -89 --> Error! Input your number >= 10!  _" + \
              str(same_num(-89) == "Error! Input your number >= 10!")
    print(result)


testing()
