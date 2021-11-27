# get a number and print a triangle with that number of lines

count = int(input("Enter a number: "))
i = 1
v = 1
while count >= i:
    v = count
    while v >= i:
        print('*', end="")
        v -= 1
    print()
    count -= 1