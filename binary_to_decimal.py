# get a number from user and convert it to decimal

b = input("Input binary number ")

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return decimal

print("GitHub Copilot :", binary_to_decimal(b))

# Me

b = input("Input binary number ")
decimal = 0
for i in range(1, len(b)+1):
    plus_add = int(b[-i]) * (2 ** (i-1))
    decimal += plus_add

print("Me :", decimal)