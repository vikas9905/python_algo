def solve(arr):
	l=[]
	for i in arr:
		factor_sum=factor(i)
		
		if factor_sum in arr:
			l.append(i)
	return l

def factor(num):
	prime_factor=[]
	if num==1:
		return 1
	Sum=1
	i=2
	while(num>1 and i<=num//2):
		while(num%i==0):
			prime_factor.append(i)
			num=num//i
		i+=1
	if num>1:
		prime_factor.append(num)
	#print(prime_factor)
	s=set(prime_factor)
	for i in s:
		Sum*=((pow(i,(prime_factor.count(i)+1))-1)//(i-1))
	return Sum

		



def main():
	ll=list(map(int,input().split()))
	ans=solve(ll)
	print(*ans)
if __name__ == '__main__':
	main()