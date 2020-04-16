def solve(n,l):
	arr=[0]*len(l)
	for i in range(len(l)):
		arr[i]=l.count(l[i])
	while(n):
		Min=min(arr)
		ind=arr.index(Min)
		l.pop(ind)
		n-=1
	s=set(l)
	return len(s)


def main():
	n=int(input())
	ll=list(map(int,input().split()))
	ans=solve(n,ll)
	print(ans)
if __name__ == '__main__':
	main()