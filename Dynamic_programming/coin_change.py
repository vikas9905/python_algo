def coin_change(arr,n):
	table=[[0]*len(arr) for _ in range(n+1)]
	for i in range(len(arr)):
		table[0][i]=1
	for i in range(1,n+1):
		for j in range(len(arr)):
			x=table[i-arr[j]][j] if i-arr[j]>=0 else 0
			y=table[i][j-1] if j>0 else 0
			table[i][j]=x+y
	return table[n][len(arr)-1]

def main():
	n=int(input())
	m=int(input())
	arr=list(map(int,input().split()))
	count=coin_change(arr,n)
	print(count)

if __name__ == '__main__':
	main()