# coding:utf-8

def merge(l,p,q,r):
	'''合并两个已排序的子序列，产生一个排好序的新序列(in-place).

	给定一个序列l, p,q,r是序列下标，满足p<=q<r,假定子序列l[p:q+1],
	l[q+1:r]按升序排列。

	参数：
		l: 待排序的序列
		p: 序列的起始位置
		q: 满足使l[p:q+1],l[q+1:r]有序的位置
		r: 序列的结束位置(不包括)

	返回:
		无。函数调用结果是序列l[p:r]有序。
	'''
	a = l[p:q+1]
	b = l[q+1:r]
	i = 0
	j = 0

	for k in range(p,r):
		if i == q+1-p or j == r-q-1:
			break
		if a[i] < b[j]:
			l[k] = a[i]
			i += 1
		else:
			l[k] = b[j]
			j += 1

	if i == q+1-p:
		l[k:r] = b[j:len(b)]
	else:
		l[k:r] = a[i:len(a)]


def _merge_sort(l,p,r):
	if p < r-1:
		q = (p+r)//2
		_merge_sort(l,p,q)
		_merge_sort(l,q,r)
		merge(l,p,q-1,r)



def merge_sort(l):
	return _merge_sort(l,0,len(l))
