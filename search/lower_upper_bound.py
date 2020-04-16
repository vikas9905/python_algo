l=list(map(int,input().split()))
k=int(input())  #element on which to check lower and upper bound
def upper_bound(l,k):
	start=0
	end=len(l)
	while(start<end):
		mid=(start+end)//2
		if l[mid]<=k:
			start=mid+1
		else:
			end=mid
	return start
def lower_bound(l,k):
	start=0
	end=len(l)
	while(start<end):
		mid=(start+end)//2
		if l[mid]>=k:
			end=mid
		else:
			start=mid+1
	return start
def main():
	l.sort()
	ans=upper_bound(l,k)
	ans2=lower_bound(l,k)
	print(ans)
	print(ans2)
main()