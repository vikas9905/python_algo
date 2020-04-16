'''Given two integers ‘a’ and ‘m’, find modular multiplicative inverse of ‘a’ under modulo ‘m’.

The modular multiplicative inverse is an integer ‘x’ such that.

 a x ≡ 1 (mod m) 

The value of x should be in {0, 1, 2, … m-1}, i.e., in the range of integer modulo m.'''
def Extendedgcd(a,b):
	if a==0:
		return(b,0,1)
	else:
		g,y,x=Extendedgcd(b%a,a)
		return (g,x-(b//a)*y,y)

def modInverse(a,m):
	while a<0:
		a+=m
	g,x,y=Extendedgcd(a,m)
	return x%m

def main():
	n,m=map(int,input().split())
	ans=modInverse(n,m)
	print(ans)
main()
