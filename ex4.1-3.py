# coding:utf-8

def find_maximum_crossing_subarray(a, l, mid ,h):
    max_left_sum = left_sum = 0
    low = mid
    for i in range(mid,l-1,-1):
        left_sum += a[i]
        if max_left_sum < left_sum:
            max_left_sum = left_sum
            low = i

    max_right_sum = right_sum = 0
    high = mid + 1
    for k in range(mid + 1, h + 1):
        right_sum += a[k]
        if max_right_sum < right_sum:
            max_right_sum = right_sum
            high = k

    return (low, high, max_left_sum + max_right_sum)


def find_maximum_subarray(a, low, high):
    '''
    最大子数组的递归实现
    '''
    if low == high:
        return (low, high, a[low])
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(a, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(a, mid + 1, high)
    cross_low, cross_high, cross_sum = find_maximum_crossing_subarray(a, low, mid, high)

    m = max(left_sum, right_sum, cross_sum)
    if m == left_sum:
        return (left_low, left_high, left_sum)
    elif m == right_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)

if __name__ == '__main__':
    a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    *_, max_sum = find_maximum_subarray(a, 0, len(a)-1)
    print(max_sum)