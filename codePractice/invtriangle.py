for i in range(4, 0, -1):
    for j in range(0, 4-i):
        print(end=" ")
    for k in range(0, i):
        print("*", end=" ")
    print()