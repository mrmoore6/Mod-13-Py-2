import math
import sympy
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibonacci(n):
    if isPerfectSquare(5 * n * n + 4) == True or isPerfectSquare(5 * n * n - 4) == True:
        return True
    else:
        return False



def fibonacci_generator():
    n = 0
    while True:
        n += 1
        if isFibonacci(n):
            yield n

f = fibonacci_generator()

def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result
def prime(x):
    if sympy.isprime(x):
        return x

x = take(22, f)

y = (list(filter(prime, x)))

print(y)
