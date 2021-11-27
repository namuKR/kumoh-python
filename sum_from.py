n : int

n = int(input())
print((n*(n+1))/2)

s : int = 1
cnt = 1
while cnt <= 1000:
    s *= cnt
    cnt += 1

print(s)