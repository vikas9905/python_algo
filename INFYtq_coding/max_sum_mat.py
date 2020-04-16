import math

def solve(mat):
	n=len(mat)
	max_sum=0
	l_max=[]
	dp=[[0]*n for _ in range(n)]
	for i in range(n):
		dp[0][i]=mat[0][i]
	for i in range(1,n):
		for j in range(0,n):
			dp[i][j]=mat[i-1][j]+mat[i][j]
	for i in range(1,n):
		Sum=0
		for j in range(1,n):
			Sum=dp[i][j]+dp[i][j-1]
			if max_sum<=Sum:
				l_max.append([i,j])
	for i in l_max:
		for i in l


def main():
	arr=list(map(int,input().split(',')))
	n=len(arr)
	m=int(math.sqrt(n))
	mat=[]
	k=0
	for i in range(m):
		mat.append(arr[k:k+m])
		k+=3
	solve(mat)
if __name__ == '__main__':
	main()
