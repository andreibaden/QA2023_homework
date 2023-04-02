# Task10.6 "The palindrome"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def pal(num):
    if int(num) <= 0:
        return "Error! Input correct number > 0!"

    for i in range(len(num) // 2):
        if num[i] != num[- i - 1]:
            return "NO"
    return "YES"


def main():
    number = input("Input your number > 0: ")
    msg = pal(number)
    print(msg)


main()


def testing():
    result = " 131 --> YES _" + str(pal(str(131)) == "YES")
    result += "\n 537 --> NO _" + str(pal(str(537)) == "NO")
    result += "\n -3 --> Error! Input correct number > 0! _" + \
              str(pal(str(-3)) == "Error! Input correct number > 0!")
    print(result)


testing()
