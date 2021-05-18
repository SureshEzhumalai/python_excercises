# num = 1
# for row in range(1,6):
#     for col in range(1, row + 1):
#         print(num , end=" ")
#         num = num + 1
#     print()


val = 1
for row in range(5):

    inc = 5
    for col in range(row + 1):
        print(val, end=" ")
        val = row + 1
        inc = inc - 1

    print()
