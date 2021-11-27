# get two numbers and get lowest common multiple


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

    ###########################################

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(1, a*b+1):
    if i % a == 0 and i % b == 0:
        print("LCM =",i)
        break