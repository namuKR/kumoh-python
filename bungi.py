num = int(input("Input number? "))
num_range : int
if num <= 10:
    num_range = 10
else:
    if num <= 100:
        num_range = 100
    
    else:
        num_range = 1000

print("정수 %d는 %d 이하입니다.\n종료합니다" % (num, num_range))