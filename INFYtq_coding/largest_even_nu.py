import re
def solve(s):
	p=re.compile('[0-9]')
	arr=p.findall(s)
	arr=[int(i) for i in arr]
	arr=set(arr)
	l=list(arr)
	l.sort()
	ind=c=0
	if len(l)>0:
		if l[0]%2!=0:

			for i in range(1,len(l)):
				if l[i]%2==0:
					ind=i
					c+=1
					break
			if c==0:
				return -1
	l[0],l[ind]=l[ind],l[0]
	return ''.join(str(i) for i in l[::-1])


def main():
	s=input()
	ans=solve(s)
	print(ans)

if __name__ == '__main__':
	main()