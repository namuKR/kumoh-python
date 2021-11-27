def isPrime(p):
    import math
    for i in range(2, math.ceil(math.sqrt(p))):
        if p % i == 0:
            return False
    return True

p = int(input("Enter a number: "))
print("Is Prime?",isPrime(p))