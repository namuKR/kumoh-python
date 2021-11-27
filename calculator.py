def calculator(num1, num2):
    return num1+num2, num1-num2, num1*num2, num1/num2

s = calculator(10, 20)
print("Sum is",s[0])
print("Subtract is", s[1])
print("Multiply is", s[2])
print("Divide is", s[3])