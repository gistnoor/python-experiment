import random

def fac(n):
    if n == 0:
        return 1
    else:
        return (fac(n-1) * n)

def permutations(items):
    n = len(items)
    if n == 0 : yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]] + cc

def k_permutations(items, n):
    if n == 0: yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n-1):
                if (not items[i] in ss):
                    yield [items[i]] + ss

de