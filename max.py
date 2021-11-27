# declare function get four numbers and print the max


def get_max(num1, num2, num3, num4):
    if num1 > num2:
        return num1
    else:
        return num2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
print(get_max(get_max(a,b), get_max(c,d)))

#####
def get_max(num1, num2, num3, num4):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4

    return max_num

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

print(get_max(a, b, c, d))
#####