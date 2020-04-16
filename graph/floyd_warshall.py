def main():
	t=int(input())
	while(t):
		vertex=int(input())
		arr=[list(map(float,input().split())) for _ in range(vertex)]
		for k in range(vertex):
			for i in range(vertex):
				for j in range(vertex):
					if arr[i][j]>arr[i][k]+arr[k][j]:
						arr[i][j]=arr[i][k]+arr[k][j]
		for i in range(vertex):
			for j in range(vertex):
				print(int(arr[i][j]),end=" ") if arr[i][j]!=float('INF') else print("INF",end=" ")
			print()
		t-=1
if __name__ == '__main__':
	main()
