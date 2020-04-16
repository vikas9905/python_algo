def combination(n,k):
	c=[0]*(k+1)
	c[0]=1
	for i in range(1,n+1):
		for j in range(min(i,k),0,-1):
			c[j]=c[j]+c[j-1]
	return c[k]

def main():
	n=int(input())
	k=int(input())
	res=combination(n,k)
	print("n_c_k={}".format(res))

if __name__ == '__main__':
	main()