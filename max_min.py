from builtins import max as ma, min as mi
def maximum(a):
    max = a[0]
    for i in range(1,len(a)):
        if max < a[i]:
            max = a[i]
    return max

def minimum(a):
    min = a[0]
    for i in range(1,len(a)):
        if min > a[i]:
            min = a[i]
    return min

def min_max(a):
    # len(a) is odd
    if len(a) & 1:
        min = max =a[0]
        b = ((a[i], a[i+1]) for i in range(1, len(a), 2))
    else:
        min = mi(a[0:2])
        max = ma(a[0:2])
        b = ((a[i], a[i+1]) for i in range(2, len(a), 2))

    for i, v in enumerate(b):
        min = mi(min, mi(v))
        max = ma(max, ma(v))

    return min, max


