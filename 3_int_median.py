num1 = int(input("Input 1st number? "))
num2 = int(input("Input 2nd number? "))
max_num = num1
min_num = num2


if max_num < min_num:
    max_num, min_num = min_num, max_num

num3 = int(input("Input 3rd number? "))
if max_num >= num3 >= min_num:
    median = num3
elif num3 > max_num:
    median = max_num
elif min_num > num3:
    median = min_num

print(f"Median of {num1}, {num2}, {num3} is {median}")