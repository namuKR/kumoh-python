p = int(input("Enter a number: "))

import math
for i in range(2, math.ceil(math.sqrt(p))):
    if p % i == 0:
        print("Not prime")
        exit()
print(p,'is prime')