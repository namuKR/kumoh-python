# num1 = int(input("Input 1st number? "))
# num2 = int(input("Input 2nd number? "))

# max_num = num1 if num1 > num2 else num2

# num3 = int(input("Input 3rd number? "))
# num4 = int(input("Input 4th number? "))

# min_num = num3 if num3 < num4 else num4

# if max_num < min_num:
#     max_num, min_num = min_num, max_num

# # num = int(input(f"input 1 "))
# # max_num = num
# # min_num = num
# # for i in range(9):
# #     num2 = int(input(f"Input {i+1} "))
# #     if max_num < num2:
# #         max_num = num2
# #     if min_num > num2:
# #         min_num = num2

num1 = int(input("Input 1st number? "))
max_num = num1
min_num = num1

num2 = int(input("Input 2nd number? "))
if max_num < num2:
    max_num = num2
if min_num > num2:
    min_num = num2

...

print(f"Max is {max_num} and Min is {min_num}")

     

print(f"Max is {max_num} and Min is {min_num}")
