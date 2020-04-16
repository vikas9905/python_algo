def solve(s):
	stack=[]
	stack.append(s[0])
	j=1
	ans=0
	i=0
	while(len(s)>=i and j<len(s)):
		if s[j]=='(' or s[j]=='{' or s[j]=='[':
			stack.append(s[j])
			j+=1
		else:
			if len(stack)==0:
				return j+1
			Open=stack.pop()
			if check_pair(Open,s[j]):
				j+=1
			else:
				j+=1
				ans=j
				break
		i+=1
	if len(stack)!=0:
		ans=j+1
	return ans




def check_pair(o,c):
	if o=='(' and c==')':
		return 1
	elif o=='{' and c=='}':
		return 1
	elif o=='[' and c==']':
		return 1
	else:
		return 0


def main():
	s=input()
	ans=solve(s)
	print(ans)

if __name__ == '__main__':
	main()