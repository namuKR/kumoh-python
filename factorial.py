n = int(input("Enter a number: "))

i = 1
a = 1
s = 0
while i <= n:
    a = a * i
    s += a
    i = i + 1

print(s)