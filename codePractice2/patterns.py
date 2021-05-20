# printing diff star patterns using one for loop instead of two

num = int(input("Enter the number: "))

# square
for row in range(num):
    print("* " * num)

# right triangle
for i in range(num):
    print("* " * (i+1))

# right triangle 2
for i in range(num):
    print("  " * (num-i), "* " * (i+1))

#triangle

for i in range(num):
    print(" " * (num-i), "* " * (i+1))

# inv triangle
for i in range(num, 0, -1):
    print(" " * (num-i), "* " * (i))


# diamond
for i in range(num):
    print(" " * (num-1-i), "* " * (i+1))
for i in range(num-1, 0, -1):
    print(" " * (num-i), "* " * (i))

# inv triangle
for i in range(num):
    print("* " * (num - i))

# arrow
for i in range(num):
    print("* " * (i+1))
for i in range(num):
    print("* " * (num-1 - i))