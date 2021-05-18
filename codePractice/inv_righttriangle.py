for i in range(0, 5):
    print("* " * (5-i))

# another method

for i in range(5, 0, -1):
    print("* " * i)

# using two loops
for i in range(0, 5):
    for j in range(5-i, 0 , -1):
        print("*", end=" ")
    print()