def solve(s):
	s2=s
	s2=s2.lower()
	size=-1
	l=['']*26
	for i in range(len(s)):
		ind=ord(s2[i])-ord('a')
		l[ind]+=s[i]
	s2=list(s2)
	s2=set(s2)
	s2=list(s2)
	s2.sort()
	print(s2)
	str1=""
	if len(s2)%2==0:
		size=len(s2)//2
	else:
		size=len(s2)//2+1
	for i in range(size):
		ind1=ord(s2[i])-ord('a')
		ind2=ord(s2[-(i+1)])-ord('a')
		if ind1==ind2:
			str1+=l[ind1]
			continue
		str1+=l[ind1]+l[ind2]
	print(str1)


def main():
	s=input()
	ans=solve(s)
if __name__ == '__main__':
	main()