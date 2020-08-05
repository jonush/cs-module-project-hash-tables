import math
import random
import functools

def slowfun_too_slow(x, y):
    v = math.pow(x, y)      # v = xʸ
    v = math.factorial(v)   # v!
    v //= (x + y)           # v // (x + y)
    v %= 982451653          # v % 982451653

    return v

cache = {}

# @functools.lru_cache(maxsize=None)
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # p = math.pow(x, y)
    # f = math.factorial(p)
    # q = f // (x + y)
    # return q % 982451653

    # if p is less than the max value in the cache, return that factorial and add it to the factorial of the new p up to the old one
    p = math.pow(x, y)

    if p not in cache:
        cache[p] = math.factorial(p)

    q = cache[p] // (x + y)
    return q % 982451653

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
