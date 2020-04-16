def Find_cost(cost_mat,src,dest):
	r=len(cost_mat)
	c=len(cost_mat[0])
	table=[[0]*c for _ in range(r)]
	table[0][0]=max(cost_mat[0])#[0]
	for i in range(1,src+1):
		table[i][0]=table[i-1][0]+cost_mat[i][0]
	for i in range(1,dest+1):
		table[0][i]=table[0][i-1]+cost_mat[0][i]
	for i in range(1,src+1):
		for j in range(1,dest+1):
			table[i][j]=max(table[i][j-1],table[i-1][j],table[i-1][j-1])+cost_mat[i][j]
	return table[src][dest]

def main():
	n=int(input("enter row\n"))
	cost_mat=[list(map(int,input().split())) for _ in range(n)]
	src,dest=map(int,input().split())
	min_cost=Find_cost(cost_mat,src-1,dest-1)
	print(min_cost)
if __name__ == '__main__':
	main()