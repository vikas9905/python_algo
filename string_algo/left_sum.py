def solve(s):
	total=[0]*(len(s)+1)
	for i in range(1,len(s)):
		total[i]=int(s[i])
	l=2
	ans=0
	while l<=len(s):
		for i in range(len(s)-l+1):
			if(total[i+int(l/2)]-total[i]==total[i+1]-total[i+int(l/2)]):
				print(total[i],total[i+int(l/2)],total[i+int(l/2)]-total[i],sep=" ")
				print(total[i+1])
				ans=max(ans,l)
		l+=2
	return ans

def main():
	t=int(input())
	while(t):
		s=input()
		res=solve(s)
		print(res)
		t-=1
if __name__ == '__main__':
	main()