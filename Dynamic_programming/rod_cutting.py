def max_proffit(arr):
	n=len(arr)
	val=[0]*(n+1)
	val[0]=0
	for i in range(1,n+1):
		max_len=-5555
		for j in range(i):
			max_len=max(max_len,arr[j]+val[i-j-1])
		val[i]=max_len
	print(val)
	return val[n]


def main():
	arr=list(map(int,input().split()))
	max_len=max_proffit(arr)
	print(max_len)
if __name__ == '__main__':
	main()