for i in range(0, 5):
    print("*" * (i+1))

# using two loops
for i in range(0, 5):
    for j in range(i+1):
        print("*", end="")
    print()
