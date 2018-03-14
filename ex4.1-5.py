# coding:utf-8

def find_maximum_subarray(a):
    '''线性时间找到最大子数组'''
    max = sum = 0
    cur_low = 0
    max_low = max_high = -1
    for i in range(len(a)):
        sum += a[i]
        if sum < 0:
            sum = 0
            cur_low = i + 1

        if sum > max:
            max_low = cur_low
            max_high = i
            max = sum
    return (max_low, max_high, max)

if __name__ == '__main__':
    a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    sum, l, h= find_maximum_subarray(a)
    print("sum of maximum subarray is %d, from %d to %d" %(sum, l, h))