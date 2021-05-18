string = input("Enter the desired string: ")

for row in range(len(string)):
    for col in string[0:row +1]:
        print(col, end="")
    print()