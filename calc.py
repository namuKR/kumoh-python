num1 = float(input("Input number1? "))
num2 = float(input("Input number2? "))
operator = input("Input operator? ")
# ans: float
# if operator not in ['+', '-', '*', '/']:
#     raise TypeError("operator not valid")

# if operator == "+":
#     ans = num1+num2
# elif operator == '-':
#     ans = num1-num2
# elif operator == '*':
#     ans = num1*num2
# else:
#     if num2 != 0:
#         ans = num1/num2
#     else:
#         print("cannot divide to zero")
    
# print(f"{num1}{operator}{num2} = {ans}")
print(eval(f"{num1}{operator}{num2}"))