for row in range(6):
    for col in range(6):
        if row == 0 or row == 5 or (row + col == 5 and (0 < row < 5)):
            print("*", end="")
        else:
            print(end=" ")
    print()