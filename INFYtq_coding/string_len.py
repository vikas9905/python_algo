def solve(arr):
	ans=''
	for i in range(len(arr)):
		string=arr[i][0]
		ind=-1
		ll=[int(j) for j in arr[i][1]]
		len_string=len(string)
		for j in sorted(ll):
			if max(ll)==len_string:
				ind=max(ll)
				break
			if min(ll)>len_string:
				ans+='X'
				break
			if j==len_string:
				ind=j
				break
			elif j<len_string:
				ind=j
			else:
				continue
		if(min(ll)>len_string):
			continue
		ans=ans+arr[i][0][ind-1]
	return ans



def main():
	s=input()
	arr=s.split(',')
	arr2=[i.split(':') for i in arr]
	print(arr2)
	string=solve(arr2)
	print(string)
if __name__ == '__main__':
	main()
