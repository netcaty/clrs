# coding:utf-8

from merge_sort import *

def has_sum(a,s):
    h = 0
    t = len(a) - 1
    merge_sort(a)
    while h < t :
        sum = a[h] + a[t]
        if sum == s:
            return (True, h, t)
        if sum < s:
            h += 1
        else :
            t -= 1
    return False, -1, -1

if __name__ == '__main__':
    a = [3, 41, 52, 26, 38, 57, 9, 49]
    for x in range(100):
        i,j,k = has_sum(a,x)
        if i is True:
            print('%s has two elements (%d, %d).sum of them is %d' % (a,a[j],a[k],x))