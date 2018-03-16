# coding:utf-8

def max_heapify(a, i):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(a) and a[l] > a[i]:
            largest = l
        else:
            largest = i
        if r < len(a) and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            i = largest
        else:
            break


if __name__ == '__main__':
    pass
