def solve(l):
	ans=[]
	for i in range(0,len(l)-1):
		for j in range(0,len(l)-1):
			e1=l[i][j]
			e2=l[i][j+1]
			e3=l[i+1][j]
			e4=l[i+1][j+1]
			if e1%sum_of_digit(e1)==0 and e2%sum_of_digit(e2)==0 and e3%sum_of_digit(e3)==0 and e4%sum_of_digit(e4)==0:
				ans.append([e1,e2])
				ans.append([e3,e4])
	for i in ans:
		for j in i:
			print(j,end=" ")
		print("")
def sum_of_digit(num):
	st=str(num)
	l=list(st)
	Sum=0
	for i in l:
		Sum+=int(i)
	return Sum

def main():
	n=int(input())
	l=[list(map(int,input().split())) for i in range(n)]
	solve(l)
if __name__ == '__main__':
	main()