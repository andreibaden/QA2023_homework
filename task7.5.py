# Task7.5 "Vowels"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 01.03.2023


def vowel(letter):
    if letter == "a" or letter == "e" or letter == "i" or \
            letter == "o" or letter == "u" or letter == "y":
        answer = "This is vowel!"
    else:
        answer = "This is not vowel!"

    return answer


def main():
    letter = str(input("Input English letter: "))
    msg = vowel(letter)
    print(f"\n Your letter is {letter}.\n {msg}")


main()


def testing():
    result = " d --> " + str(vowel("d") == "This is not vowel!")
    result += "\n a --> " + str(vowel("a") == "This is vowel!")
    result += "\n o --> " + str(vowel("o") == "This is vowel!")

    print(result)


testing()
