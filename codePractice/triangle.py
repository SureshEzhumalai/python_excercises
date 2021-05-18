for i in range(0, 4):
    for j in range(0, 4-i-1):
        print(" ", end=" ")
    for k in range(0, i+1):
        print("* ", end=" ")
    print()

# another method

for i in range(0, 4):
    print(" " * (4-i-1) + "* " * (i+1))