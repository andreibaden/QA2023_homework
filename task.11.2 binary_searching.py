def binary_searching(ls, value):
    first = 0
    last = len(ls) - 1

    while first <= last:
        middle = (first + last) // 2
        if ls[middle] == value:
            return True
        elif ls[middle] < value:
            first = middle + 1
        else:
            last = middle - 1

    return False

ls = [2,4,5,7,9,2,4]
print(binary_searching(ls, 3))
print(binary_searching(ls, 2))
print(binary_searching(ls, 70))
