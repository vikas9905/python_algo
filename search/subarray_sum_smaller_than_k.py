n,k=map(int,input().split())
l=list(map(int,input().split()))
dp=[0]
for i in range(1,n+1):
	dp.append(sum(l[:i]))

ans=-1
l=1
r=n
while(l<=r):
	mid=(l+r)//2
	flag=1
	for i in range(mid,n+1):
		if (dp[i]-dp[i-mid])>k:
			flag=0
			break
	if flag:
		l=mid+1
		ans=mid
	else:
		r=mid-1
print(ans)


