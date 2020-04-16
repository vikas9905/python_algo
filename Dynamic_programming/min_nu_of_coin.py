''' find min number of coin to give change'''
def solve(value,coins):
	ans=[]
	coins.sort(reverse=True)
	for i in range(len(coins)):
		while value>=coins[i]:
			ans.append(coins[i])
			value-=coins[i]
	print(ans,value)
	return len(ans)


def main():
	value=int(input())
	coins=list(map(int,input().split()))
	ans=solve(value,coins)
	print(ans)
if __name__ == '__main__':
	main()