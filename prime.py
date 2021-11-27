p = int(input("enter number: "))

import math
i = 2
while p % i != 0:
    for i in range(2, p):
        if p % i == 0:
            print(p, "is not a prime number")
            break
    if i == p - 1:
        print(p, "is a prime number")
        break