for row in range(8):
    for col in range(5):
        if ((col == 0 or col == 4) and (0 < row < 6)) or ((row == 0 or row == 6) and (0 < col < 4)) or (
                (row == 5 and col == 1) or (row == 7 and col == 4)
        ):
            print("*", end="")
        else:
            print(end=" ")
    print()
