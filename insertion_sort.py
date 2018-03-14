# coding:utf-8

def insertion_sort(l):
	for j  in range(1,len(l)):
		key = l[j]
		i = j-1
		while i >= 0 and l[i] < key:
			l[i+1] = l[i]
			i -= 1
		l[i+1] = key

if __name__ == '__main__':
	a = [31, 41, 59, 26, 41, 58]
	print(a)
	insertion_sort(a)
	print(a)