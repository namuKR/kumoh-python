from ast import Index


exp = input("enter math expression: ")

items = exp.split(' ')

operators = ['+', '-', '*', '/']
operator_list = []
num = []
for item in items:
    if item in operators:
        operator_list.append(item)
    elif isinstance(int(item), int) or isinstance(float(item), float):
        num.append(float(item))
    else:
        raise TypeError("Check if you entered the right expression")

eval_exp: str = str(num[0])

for i in range(len(operator_list)):
    eval_exp += operator_list[i]
    eval_exp += str(num[i+1])

print(eval(eval_exp))