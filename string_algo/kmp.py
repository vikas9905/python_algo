def kmp(text,pat):
	lps=[0]*len(pat)
	find_lps(lps,pat)
	i=0
	j=0
	while(i<len(text) and j<len(pat)):
		if text[i]==pat[j]:
			i+=1
			j+=1
		if j==len(pat):
			print("pattern found at",i-j)
		elif i<len(text) and pat[j]!=text[i]:
			if j>0:
				j=lps[j-1]

			else:
				i+=1
	return lps

def find_lps(lps,pat):
	lps[0]=0
	i=1
	j=0
	while(len(pat)>i):
		if(pat[i]==pat[j]):
			j+=1
			lps[i]=j
			i+=1
		else:
			if j!=0:
				j=lps[j-1]
			else:
				lps[i]=0
				i+=1


def main():
	text=input()
	pat=input()
	for i in range(1,len(text)+1):
		print(kmp(text,text[:i]))
	#res=kmp(text,pat)
	#print(res)
if __name__ == '__main__':
	main()