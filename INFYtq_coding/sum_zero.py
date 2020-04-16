from itertools import combinations
def solve(ll):
	ll2=combinations(ll,4)
	count=0
	for i in ll2:
		if sum(i)==0:
			count+=1
	return count


def main():
	ll=list(map(int,input().split()))
	ans=solve(ll)
	print(ans)
if __name__ == '__main__':
	main()