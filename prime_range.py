n = int(input("Enter a number: "))
v = []
i = 2
while True:
    for t in range(2, i):
        if i % t == 0:
            break
    else:
        v.append(i)
    
    if len(v) == n:
        break
    i += 1
print(v)