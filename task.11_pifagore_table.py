def pifagore_table(size):
    table = ""

    for multy in range(1, size + 1):
        for item in range(1, size + 1):
            table += str(item * multy) + "\t"
        table += "\n"
        multy += 1

    return table


print(pifagore_table(7))
