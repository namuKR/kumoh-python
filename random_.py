import random

def return_rand_int():
    randint = int(random.random()*39+10)
    return randint

random_num = return_rand_int()

print(
    f"""
    N % 2 = {random_num%2}
    N % 3 = {random_num%3}
    N % 5 = {random_num%5}
    N % 7 = {random_num%7}
    N % 11 = {random_num%11}
    """
)
num = int(input("Input number (10~49) ? "))
if num == random_num:
    print("Correct!")
else:
    print("Wrong! answer is", random_num)