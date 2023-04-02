# Task7.6 "Age"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 05.03.2023


def age(number):
    age_100 = str()
    age_1_20 = str()
    age_20_90 = str()

    if number > 120 or number <= 0:
        return "Error! Input correct number!"
    else:
        if number % 100 == 0 and number > 1:
            return "Your age is сто лет!"
        elif number // 100 == 1 and number > 100:
            age_100 = "сто "

        if (number // 10 == 12 or number // 10 == 2) and number % 10 > 0:
            age_20_90 = "двадцать "
        elif number // 10 == 3:
            age_20_90 = "тридцать "
        elif number // 10 == 4:
            age_20_90 = "сорок "
        elif number // 10 == 5:
            age_20_90 = "пятьдесят "
        elif number // 10 == 6:
            age_20_90 = "шестьдесят "
        elif number // 10 == 7:
            age_20_90 = "семьдесят "
        elif number // 10 == 8:
            age_20_90 = "восемьдесят "
        elif number // 10 == 9:
            age_20_90 = "девяноста "
        age_20_90 = age_20_90 + str("лет") if number % 10 == 0 and \
        91 > number > 20 else age_20_90

        if (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 1:
            age_1_20 = "один год"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 2:
            age_1_20 = "два года"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 3:
            age_1_20 = "три года"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 4:
            age_1_20 = "четыре года"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 5:
            age_1_20 = "пять лет"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 6:
            age_1_20 = "шесть лет"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 7:
            age_1_20 = "семь лет"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 8:
            age_1_20 = "восемь лет"
        elif (100 < number < 110 or 20 < number < 100 or number < 10) and \
                number % 10 == 9:
            age_1_20 = "девять лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 0:
            age_1_20 = "десять лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 1:
            age_1_20 = "одиннадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 2:
            age_1_20 = "двеннадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 3:
            age_1_20 = "тринадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 4:
            age_1_20 = "четырнадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 5:
            age_1_20 = "пятнадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 6:
            age_1_20 = "шестнадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 7:
            age_1_20 = "семнадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 8:
            age_1_20 = "восемнадцать лет"
        elif (number // 10 == 11 or number // 10 == 1) and number % 10 == 9:
            age_1_20 = "девятнадцать лет"
        elif (number // 10 == 12 or number // 10 == 2) and number % 10 == 0:
            age_1_20 = "двадцать лет"
        age_finish = "Your age is " + age_100 + age_20_90 + age_1_20 + "!"
        return age_finish



# def main():
#     number = int(input("Input your age: "))
#     msg = age(number)
#
#
#     print(f"\n{msg}")
#
#
# main()

def testing():
    result = " -5 --> " + str(age(-5) == "Error! Input correct number!")
    result += "\n 0 --> " + str(age(0) == "Error! Input correct number!")
    result += "\n 121 --> " + str(age(121) == "Error! Input correct number!")
    result += "\n 2 --> " + str(age(2) == "Your age is два года!")
    result += "\n 9 --> " + str(age(9) == "Your age is девять лет!")
    result += "\n 10 --> " + str(age(10) == "Your age is десять лет!")
    result += "\n 17 --> " + str(age(17) == "Your age is семнадцать лет!")
    result += "\n 60 --> " + str(age(60) == "Your age is шестьдесят лет!")
    result += "\n 78 --> " + str(age(78) == "Your age is семьдесят восемь лет!")
    result += "\n 100 --> " + str(age(100) == "Your age is сто лет!")
    result += "\n 101 --> " + str(age(101) == "Your age is сто один год!")
    result += "\n 115 --> " + str(age(115) == "Your age is сто пятнадцать лет!")
    result += "\n 120 --> " + str(age(120) == "Your age is сто двадцать лет!")
    print(result)


testing()
