def solve(arr):
	count=0
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if check(arr[i],arr[j]):
				print(arr[i],arr[j],sep=" ")
				count+=1

	return count
def check(num1,num2):
	s1=str(num1)
	s2=str(num2)
	s1=[int(i) for i in s1]
	s2=[int(i) for i in s2]
	if sum(s1)==sum(s2):
		return 1
	else:
		return 0

def main():
	arr=list(map(int,input().split()))
	ans=solve(arr)
	print(ans)
if __name__ == '__main__':
	main()
