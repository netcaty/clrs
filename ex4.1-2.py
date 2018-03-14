# coding:utf-8

def find_maximum_subarray(a):
    max_sum = 0
    l = h = -1
    for i in range(len(a)):
        sum = 0
        for k in range(i,len(a)):
            sum += a[k]
            if max_sum < sum:
                max_sum = sum
                l, h = i, k

    return (l, h, max_sum)

if __name__ == '__main__':
    a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    l ,h ,max_sum = find_maximum_subarray(a)
    print("max subarray sum is %d, from %d to %d" % (max_sum, l ,h))