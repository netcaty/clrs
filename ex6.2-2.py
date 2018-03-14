# coding:utf-8

def min_heapify(a, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(a) and a[l] < a[i]:
        largest = l
    else:
        largest = i
    if r < len(a) and a[r] < a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        min_heapify(a,largest)