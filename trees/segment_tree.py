import math
def constructUtil(ss,se,arr,st,i):
	if ss==se:
		st[i]=arr[ss]
		return arr[ss]
	mid=(ss+se)//2
	st[i]=constructUtil(ss,mid,arr,st,2*i+1)+constructUtil(mid+1,se,arr,st,2*i+2)
	return st[i]

def construct(arr):
	n=len(arr)
	height=math.ceil(math.log2(n))
	max_size=2*(2**height)-1
	st=[0]*(max_size)
	constructUtil(0,n-1,arr,st,0)
	return st

def updatevalueUtil(st,ss,se,diff,i):
	if i<0 or i>se:
		return 0
	st[i]=st[i]+diff
	if ss!=se:
		mid=(ss+se)//2
		updatevalueUtil(st,ss,mid,diff,2*i+1)
		updatevalueUtil(st,mid+1,se,diff,2*i+2)


def update_value(arr,st,ind,val):
	if ind<0 or ind>=len(arr):
		return 0
	diff=val-arr[ind]
	arr[ind]=val
	updatevalueUtil(st,0,len(arr)-1,diff,0)

def getsum(st,l,r,ss,se,si):
	if l<=ss and r>=se:
		return st[si]
	if se<l or ss>r:
		return 0
	mid=(ss+se)//2
	return getsum(st,l,r,ss,mid,2*si+1)+getsum(st,l,r,mid+1,se,2*si+2)

def main():
	arr=list(map(int,input().split()))
	st=construct(arr)
	print(st)
	l,r=map(int,input().split())
	ans=getsum(st,l,r,0,len(arr)-1,0)
	print(ans)
	update_value(arr,st,0,10)  #index to update=1   value=10
	print(st)
if __name__ == '__main__':
	main()