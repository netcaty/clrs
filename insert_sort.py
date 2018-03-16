def insert_sort(A):
    '''
    对于已排序的子数组A[0:j],从后往前依次扫描，
    将值与A[j]比较， 并向后移动一个位置，直到
    找到第一个不小于A[j]的值A[i]，将A[j]插入i处.
    如此子数组A[0:j+1]也变成有序的了.
    '''
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def insert_sort_rec(A):
    '''插入排序的递归实现'''

    _insert(A, 0, len(A))


def _insert(A, beg, end):
    if beg < end - 1:
        _insert(A, beg, end-1)
        key = A[end-1]
        i = end - 1
        while i > beg and A[i-1] >= key:
            A[i] = A[i-1]
            i -= 1
        A[i] = key
