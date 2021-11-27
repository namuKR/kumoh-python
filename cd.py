number = int(input("Input number? "))

for i in range(1, number+1):
    if number % i == 0:
        print(i, end=' ')