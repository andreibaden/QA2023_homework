# Task10.2 "Same numbers"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def same_num(num):
    if num <= 9:
        return "Error! Input your number >= 10!"

    while num > 9:
        flag = True
        last_digit = num % 10
        last2_digit = num % 100 // 10
        if last_digit != last2_digit:
            flag = False
            break
        num //= 10
    return flag


def main():
    number = int(input("Input your number >= 10: "))
    msg = "Error! Input your number >= 10!" if same_num(number) == \
        "Error! Input your number >= 10!" else ("YES" if "YES" else "NO")
    print(msg)


main()


def testing():
    result = " 222 --> YES _" + str(same_num(222) == "YES")
    result += "\n 345 --> NO _" + str(same_num(345) == "NO")
    result += "\n 9 --> Error! Input your number >= 10!  _" + \
              str(same_num(9) == "Error! Input your number >= 10!")
    result += "\n -89 --> Error! Input your number >= 10!  _" + \
              str(same_num(-89) == "Error! Input your number >= 10!")
    print(result)


testing()
