acc = 0
cnt = 1
while cnt <= 5:
    acc += int(input(f"input number {cnt} "))
    cnt += 1
print('합:', acc)
print('평균:',acc/5)