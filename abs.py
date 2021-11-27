# define a function and get the absolute value of a number


def abs(x):
    if x >= 0:
        return x
    else:
        return -x

x = int(input("Enter a number: "))
print(abs(x))