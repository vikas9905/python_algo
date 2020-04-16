'''In a daily share trading, a buyer buys shares in the morning and sells it on the same day. 
If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction 
can only start after the first one is complete (Sell->buy->sell->buy). Given stock prices throughout the day, 
find out the maximum profit that a share trader could have made.'''

def solve(arr):
	n=len(arr)
	profit=[0]*n

	max_price=arr[n-1]
	for i in range(n-2,0,-1):
		if max_price<arr[i]:
			max_price=arr[i]
		profit[i]=max(profit[i+1],max_price-arr[i])
	min_price=arr[0]
	for i in range(1,n):
		if min_price>arr[i]:
			min_price=arr[i]
		profit[i]=max(profit[i-1],profit[i]+(arr[i]-min_price))
	return profit[n-1]

def main():
	arr=list(map(int,input().split()))
	max_price=solve(arr)
	print(max_price)

if __name__ == '__main__':
	main()