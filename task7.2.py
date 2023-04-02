# Task7.2 "the Dragon"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 02.03.2023

def age_dragon(age):
    if age <= 0:
        return "Error! Input correct number!"

    if age < 200:
        heads = 3 + age * 3
    elif age < 300:
        heads = 203 + age * 2
    else:
        heads = 503 + age
    return heads


def main():
    age = int(input("Please,input dragon age: "))
    dragon_heads = age_dragon(age)
    dragon_eyes = dragon_heads * 2

    print(f"\n The dragon heads is {dragon_heads}.\n The dragon eyes is {dragon_eyes}!")


main()


def testing():
    result = "-1 /dragon_heads/ --> " + str(age_dragon(-1) == "Error! Input correct number!")
    result += "\n 12 /dragon_heads/ --> " + str(age_dragon(12) == 39)
    result += "\n 223 /dragon_heads/ --> " + str(age_dragon(223) == 649)
    result += "\n 355 /dragon_heads/ --> " + str(age_dragon(355) == 858)
    result += "\n 100 heads = 606 eyes --> " + str(age_dragon(100) * 2 == 606)


    print(result)


testing()
