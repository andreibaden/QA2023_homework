# Task7.3 "Multiple"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 05.03.2023

def multiple(num_n, num_m):
    if num_m == 0:
        return "Error! Input correct number!"

    if num_n % num_m == 0:
        answer = "a multiple"
    else:
        answer = "not a multiple"
    return answer


def main():
    num_n = int(input("Please,input your number: "))
    num_m = int(input("Please,input your number: "))
    msg = multiple(num_n, num_m)
    print(f"\n The number {num_n} is {msg} of the number {num_m}!")


main()


def testing():
    result = "-15 and 5 --> " + str(multiple(-15, 5) == "a multiple")
    result += "\n0 and 8 --> " + str(multiple(0, 8) == "a multiple")
    result += "\n100 and 10 --> " + str(multiple(100, 10) == "a multiple")
    result += "\n51 and 8 --> " + str(multiple(51, 8) == "not a multiple")
    result += "\n13 and 0 --> " + str(multiple(13, 0) == "Error! Input correct number!")

    print(result)


testing()
