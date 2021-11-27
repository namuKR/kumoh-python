a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(max(a,b), 1, -1):
    if a % i == 0 and b % i == 0:
        print("GCD:", i)
        break