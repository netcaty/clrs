# coding:utf-8

#左闭右开区间l[p...r]
#len a = q-p +1  len b = r-q
def merge(l,p,q,r):
	a = l[p:q+1]
	b = l[q+1:r+1]  
	i = 0
	j = 0
	cnt = 0
	for k in range(p,r+1) :
		if i == q-p+1 or j == r-q:
			break
		if a[i] <= b[j]:
			l[k] = a[i]
			i +=1
		else :
			l[k] = b[j]
			j += 1
			cnt += len(a)-i
	if i == q-p+1 :
		l[k:r+1] = b[j:]
	else :
		l[k:r+1] = a[i:]

	return cnt

def _merge_sort(l,p,r):
	i = 0
	if p < r:
		q = (p+r)//2
		i += _merge_sort(l,p,q)
		i += _merge_sort(l,q+1,r)
		i += merge(l,p,q,r)
	return i
	

def merge_sort(l):
	return _merge_sort(l,0,len(l)-1)