s = 0
cnt = 1

while True:
    if cnt > 100:
        break
    if cnt % 2 == 0:
        cnt += 1
        continue
    s += cnt
    cnt += 1

print(s)