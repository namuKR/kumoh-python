# define factorial function


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

###############################################################################
result = 1
def factorial(n):
    global result
    for i in range(1, n+1):
        result = i * result

    return result

print(factorial(5))

###############################################################################
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        