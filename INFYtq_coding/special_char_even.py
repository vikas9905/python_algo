import re

def solve(string,l,odd_even):
	str1=''
	size=len(string)
	odd=[]
	even=[]
	merge_list=[]
	odd_or_even=odd_even
	for i in range(len(l)):
		if int(l[i])%2==0:
			even.append(l[i])
		else:
			odd.append(l[i])
	print(odd)
	print(even)
	
	if odd_or_even%2==0:
		for i in range(len(l)):
			if i%2==0 and len(even)!=0:
				merge_list.append(even.pop(0))
				
			elif i%2!=0 and len(odd)!=0:
				merge_list.append(odd.pop(0))
	else:
		for i in range(len(l)):
			if i%2==0 and  len(odd)!=0:
				merge_list.append(odd.pop(0))
			elif i%2!=0 and len(even)!=0:
				merge_list.append(even.pop(0))
	if len(even)!=0:
		for i in even:
			merge_list.append(i)
	if len(odd)!=0:
		for i in odd:
			merge_list.append(i)
	str1=''.join(merge_list)
	print(merge_list)
	print(str1)





def main():
	string=input()
	p=re.compile('[0-9]')
	q=re.compile('[a-z]',re.IGNORECASE)
	l=p.findall(string)
	l2=q.findall(string)
	len_spl_char=len(string)-(len(l)+len(l2))
	ans=solve(string,l,len_spl_char)
	print(len_spl_char,l2)
if __name__ == '__main__':
	main()