arr=list(map(int,input().split(',')))
def generate(ele1,ele2,arr):
	dp=[]
	dp.append(ele1)
	dp.append(ele2)
	i=2
	while(True):
		if (dp[i-1]+dp[i-2]) in arr:
			dp.append(dp[i-1]+dp[i-2])
			i+=1
		else:
			break
	return dp
ll=[]
max_len=-1
for i in range(len(arr)-1):
	l=generate(arr[i],arr[i+1],arr)
	if i==0:
		ll.append(l)
	else:
		if max_len<len(l):
			max_len=len(l)
			ll.append(l)
if len(ll[0])<len(ll[1]):
	ll.pop(0)
ll.sort()
print(*ll[0],sep=",")
