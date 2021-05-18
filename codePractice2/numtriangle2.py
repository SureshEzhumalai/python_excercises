for row in range(5):
    val = row + 1
    inc = 5 - 1
    for col in range(row + 1):
        print(val, end="  ")
        val = val + inc
        inc = inc - 1
    print()
