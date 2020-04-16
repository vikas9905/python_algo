'''Given an array of positive integers. The task is to print the maximum length of Bitonic subsequence. 
a subsequenceof array is called Bitonic if it is first increasing, then decreasing.'''

def longest_bitcoin(arr):
	n=len(arr)
	lis=LIS(arr)
	lds=LDS(arr)
	print(lis)
	print(lds)

def LIS(arr):
	lis=[0]*(len(arr)+1)
	lis[0]=arr[0]
	size=1
	for i in range(1,len(arr)):
		if lis[0]>arr[i]:
			lis[0]=arr[i]
		elif arr[i]>lis[size-1]:
			lis[size]=arr[i]
			size+=1
		else:
			lis[Ceil(lis,-1,size-1,arr[i])]=arr[i]

	return lis

def LDS(arr):
	lis=[0]*(len(arr)+1)
	#arr=arr[::-1]
	lis[0]=arr[0]
	size=1
	for i in range(1,len(arr)):
		if lis[0]<arr[i]:
			lis[0]=arr[i]
		elif arr[i]<lis[size-1]:
			lis[size]=arr[i]
			size+=1
		else:
			lis[Ceil(lis,-1,size-1,arr[i])]=arr[i]

	return lis
def Ceil(arr,l,r,num):
	while r-l>1:
		mid=l+(r-l)//2
		if arr[mid]>=num:
			r=mid
		else:
			l=mid
	return r


def main():
	arr=list(map(int,input().split()))
	longest_bitcoin(arr)

if __name__ == '__main__':
	main()
