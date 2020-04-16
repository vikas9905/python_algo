def solve(arr):
	for i in range(len(arr)):
		ll=[int(j)*int(j) for j in arr[i][1]]
		check=sum(ll)
		#print(check)
		if check%2==0:
			l=list(arr[i][0])
			e1=l.pop()
			l.insert(0,e1)
			new_str=''.join(l)
			print(new_str,end=" ")
		else:
			l=list(arr[i][0])
			e1=l.pop(0)
			e2=l.pop(0)
			new_str=''.join(l)+e1+e2
			print(new_str)
	#for i in range(len(arr)):
	#	print(arr[i][0],end=" ")


def main():
	s=input()
	arr=s.split(',')
	arr=[i.split(':') for i in arr]
	solve(arr)
if __name__ == '__main__':
	main()
