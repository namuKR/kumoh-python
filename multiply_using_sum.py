# num1 = int(input("Input number1? "))
# num2 = int(input("Input number2? "))
# sum = 0
# for i in range(num2):
#     sum += num1

# print(sum)



for i in range(1, 10):
    for v in range(2, 10):
        print(f'{v}x{i}=%2d' % (v*i), end=' ')
    print('')