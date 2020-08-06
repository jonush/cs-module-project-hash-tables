import random

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

# compute f(x) for all possible combinations
# store the result as a key, with the value as a set
# print the set each time f(a) + f(b) = f(c)- f(d)
d = {}

for i in q:
    if i not in d:
        d[i] = f(i)

num = random.choice(q)
print(num)
print(d)