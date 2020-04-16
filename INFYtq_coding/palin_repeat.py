def solve(s):
	while(True):
		s2=s[::-1]
		if s==s2:
			return len(s)
		s+=s[::-1]

def main():
	s=input()
	ans=solve(s)
	print(ans)
if __name__ == '__main__':
	main()
