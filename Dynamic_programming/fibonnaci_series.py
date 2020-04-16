def fib1(n):
	if(n<=1):
		return n
	return fib1(n-1)+fib1(n-2)
def fib2(n,lookup):
	
	if n<=1:
		lookup[n]=n
	if lookup[n] is None:
		lookup[n]=fib2(n-1,lookup)+fib2(n-2,lookup)
	return lookup[n]
		

def main():
	n=int(input("enter nu to print fibonacci\n"))
	lookup=[None]*101
	ans1=fib1(n)
	ans2=fib2(n,lookup)
	#ans3=fib3(n)
	print(ans1,ans2,sep=" ")
if __name__ == '__main__':
	main()