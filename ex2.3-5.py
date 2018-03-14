def binsearch(A, v):
    low, high = 0, len(A)-1
    while low <= high:
        mid = (low + high) // 2
        if v < A[mid]:
            high = mid - 1
        elif v > A[mid]:
            low = mid + 1
        else:
            return mid
    return -1 # -1 means not found


from random import randrange, randint

if __name__ == '__main__':
    a = [randrange(10) for i in range(10)]
    a.sort()
    for count in range(5):
        v = int(input('What number do you find? in range (0,10):'))
        index = binsearch(a, v)
        if index == -1:
            continue
        print('found %d at %d in %s' % (v, index, a))
