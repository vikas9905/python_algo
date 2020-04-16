def solve(s):
	n=len(s)//2
	sub_str=''
	if s==s[::-1]:
		return 
	for i in range(1,n+1):
		if s[:i]==s[-i:]:
			print(s[:i])
			return i
	
	return -1



def main():
	s=input()
	ans=solve(s)
	print(ans)
if __name__ == '__main__':
	main()