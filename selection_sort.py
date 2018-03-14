# coding:utf-8

def selection_sort(a):
	n = len(a)
	for i in range(n-1):
		min = i
		for j in range(i+1,n):
			if a[min] > a[j]:
				min = j
		a[min], a[i] = a[i], a[min]

if __name__ == '__main__':
	a = [31, 41, 59, 26, 41, 58]
	print(a)
	selection_sort(a)
	print(a)