from random import randint

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

def randomized_partition(a, p, r):
    i = randint(p, r)
    a[i], a[r] = a[r], a[i]
    partition(a, p, r)

def _quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        _quicksort(a, p, q-1)
        _quicksort(a, q+1, r)

def quicksort(a):
    _quicksort(a, 0, len(a) - 1)
