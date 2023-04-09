# Task12.7 "Marks"

# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 08.04.2023


def mark_5(list):
    mark5 = 0
    for i in range(len(list)):
        if list[i] == 5:
            mark5 += 1
    return mark5


def mark_4(list):
    mark4 = 0
    for i in range(len(list)):
        if list[i] == 4:
            mark4 += 1
    return mark4


def mark_3(list):
    mark3 = 0
    for i in range(len(list)):
        if list[i] == 3:
            mark3 += 1
    return mark3


def mark_2(list):
    mark2 = 0
    for i in range(len(list)):
        if list[i] == 2:
            mark2 += 1
    return mark2


def mark_1(list):
    mark1 = 0
    for i in range(len(list)):
        if list[i] == 1:
            mark1 += 1
    return mark1


def mark_0(list):
    mark0 = 0
    for i in range(len(list)):
        if list[i] == 0:
            mark0 += 1
    return mark0


def exam_result(ls):
    q = len(ls)
    mark5 = round(mark_5(ls) * 100 / q, 1)
    mark4 = round(mark_4(ls) * 100 / q, 1)
    mark3 = round(mark_3(ls) * 100 / q, 1)
    mark2 = round(mark_2(ls) * 100 / q, 1)
    mark1 = round(mark_1(ls) * 100 / q, 1)
    mark0 = round(mark_0(ls) * 100 / q, 1)

    kl = " ".join(map(str, ls))

    result = "The Exam Result Handling"
    result += f"\nMarks: {kl}"
    result += "\nExam Result:"
    result += f"\nfives – {mark5}% ({mark_5(ls)})"
    result += f"\nfours – {mark4}% ({mark_4(ls)})"
    result += f"\n triplets – {mark3}% ({mark_3(ls)})"
    result += f"\n deuces –  {mark2}% ({mark_2(ls)})"
    result += f"\n units – {mark1}% ({mark_1(ls)})"
    result += f"\n zeros – {mark0}% ({mark_0(ls)})"
    return result


def perc_total():
    ls = [5, 4, 4, 5, 3, 4, 3, 4, 5, 3, 4, 4, 3, 4, 4, 3, 5, 3, 3, 4, 5, 5, 5, 5, 4, 5, 5, 5, 2, 5]
    print(exam_result(ls))


if __name__ == "__main__":
    perc_total()


def test():
    print("\ntest_1")
    print(exam_result([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]))
    print("\ntest_2")
    print(exam_result([5, 4, 3, 3, 2, 0]))


if __name__ == "__main__":
    test()
