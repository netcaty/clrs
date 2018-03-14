# coding:utf-8

def max_heapify(a, i, size):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and a[l] > a[i]:
            largest = l
        else:
            largest = i
        if r < size and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            i = largest
        else:
            break

def build_max_heap(a):
    for i in range(len(a)//2 - 1, -1, -1):
        max_heapify(a, i,len(a))


def heapsort(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, 0, i)

if __name__ == '__main__':
    a = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print(a)
    heapsort(a)
    print(a)