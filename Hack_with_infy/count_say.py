def generate():
	l=[[],[],[{'1':'1'}],[{'2':'1'}],[{'1':'2'},{'1':'1'}]]
	for i in range(5,31):
		s=make_str(i-1,l)
		expand_l(l,s)
	print(l[7])
	return l

def make_str(n,l):
	s=''
	for j in l[n]:
		for freq,val in j.items():
			s+=freq+val	
	return s

def expand_l(l,s):
	l2=[]
	i=0
	while(i<len(s) and i!=-1):
		count,end_pos=find_count(i,s)
		l2.append({count:s[i]})
		i=end_pos
	l.append(l2)

def find_count(ind,s):
	count=1
	end=-1
	if ind==len(s)-1:
		return ('1',ind+1)
	for i in range(ind+1,len(s)):
		if s[ind]==s[i]:
			count+=1
		else:
			end=i
			break
	return str(count),end





def main():
	n=int(input())
	l=generate()
	ans=make_str(n,l)
	print(ans)
if __name__ == '__main__':
	main()