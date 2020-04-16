import math
def longest_palindrome(s):
	n=len(s)
	if n==0:
		return
	n=2*n+1
	L=[0]*n  #position count
	L[0]=0
	L[1]=1
	c=1  #centre positio
	r=2  #centre right position
	i=0  #current right position
	imirror=0    #current left position
	max_lps_len=0
	max_lps_centre_pos=0
	start=-1
	end=-1
	diff=-1

	for i in range(2,n):
		imirror=2*c-i
		L[i]=0
		diff=r-i
		if diff>0:
			L[i]=min(L[imirror],diff)
		try:
			while(i+l[i]<n and (i-L[i])>0) and (((i+L[i]+1)%2==0) or (s[(i+L[i]+1)/2]==s[(i-L[i]-1)/2])):
				L[i]+=1
		except Exception as e:
			pass
		if L[i]>max_lps_len:
			max_lps_len=L[i]
			max_lps_centre_pos=i
		if i+L[i]>r:
			c=i
			r=i+L[i]
		start=math.floor(max_lps_centre_pos-max_lps_len)/2
		end=start+max_lps_len-1
		print(start,end)
		print("longest palin of ",s,"is",s[start:end+1])



def main():
	s=input()
	longest_palindrome(s)

if __name__ == '__main__':
	main()