def LIS(arr):
	tailTable=[0]*(len(arr)+1)
	tailTable[0]=arr[0]
	size=1
	for i in range(1,len(arr)):
		if arr[i]<tailTable[0]:
			tailTable[0]=arr[i]
		elif arr[i]>tailTable[size-1]:
			tailTable[size]=arr[i]
			size+=1
		else:
			tailTable[ceil_cal(tailTable,-1,size-1,arr[i])]=arr[i]
	return tailTable,size

def ceil_cal(arr,l,r,key):
	while(r-l>1):
		mid=l+(r-l)//2
		if arr[mid]>=key:
			r=mid
		else:
			l=mid
	return r


def main():
	arr=list(map(int,input().split(',')))
	Arr,size=LIS(arr)
	print(size)
	for i in Arr:
		print(i,end=" ")
if __name__ == '__main__':
	main()