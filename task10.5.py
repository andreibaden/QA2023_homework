# Task10.5 "Increasing sequence"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 21.03.2023

def seq_num(num):
    if num < 10:
        return "Error! Input your number > 0!"

    while num > 9:
        last_digit = num % 10
        last2_digit = num % 100 // 10
        if last_digit <= last2_digit:
            return False
        num //= 10
    return True


def main():
    number = int(input("Input your number: "))
    msg = seq_num(number)
    print(msg)


main()


def testing():
    result = " 135 --> True _" + str(seq_num(135) == True)
    result += "\n 537 --> False _" + str(seq_num(537) == False)
    result += "\n -9 --> Error! Input your number > 0! _" + \
              str(seq_num(-9) == "Error! Input your number > 0!")
    result += "\n 9 --> Error! Input your number > 0! _" + \
              str(seq_num(9) == "Error! Input your number > 0!")
    print(result)


testing()
