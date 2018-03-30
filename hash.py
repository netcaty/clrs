#!/usr/bin/env python

def log(f):
    def wrapper(*args):
        v = f(*args)
        print("{}: {}".format(args[1], v))
        return v
    wrapper.__doc__ = f.__doc__
    wrapper.__name__ = f.__name__
    return wrapper

def hash_insert(T, k, h):
    i = 0
    while i < len(T):
        j = h(T, k, i)
        if T[j] is None:
            T[j] = k
            return j
        else:
            i += 1

def linear_probe(T, k, i):
    return (aux(k) + i) % len(T)

def quad_probe(T, k, i):
    return (aux(k) + i + 3 * i ** 2) % len(T)

def aux(k):
    return k

@log
def double_hashing(T, k, i):
    return (k + i * (1 + k % (len(T) - 1))) % len(T)


if __name__ == '__main__':
    T = [None for i in range(23)]
    for i in (10, 22, 31, 4, 15, 28, 17, 88, 59):
        hash_insert(T, i, double_hashing)
