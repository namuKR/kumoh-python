import random

num1 = int(random.random() * 10)
num2 = int(random.random() * 10)

operator = random.choice(['+', '-', '*', '/'])

ans = input(f"{num1} {operator} {num2} = ")
if operator == '/':
    real_ans = num1 // num2
elif operator == '+':
    real_ans = num1 + num2
elif operator == '-':
    real_ans = num1 - num2
else:
    real_ans = num1 * num2

if int(ans) == int(real_ans):
    print("Correct")
else:
    print("Wrong ans = {}".format(real_ans))