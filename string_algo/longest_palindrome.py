def longest_palin(s):
	low=high=start=0
	max_len=1
	for i in range(len(s)):
		#for even centre
		low=i-1
		high=i
		while(low>=0 and high<len(s) and s[low]==s[high]):
			if high-low+1>max_len:
				max_len=high-low+1
				start=low
			low-=1
			high+=1
		#for odd centre
		low=i-1
		high=i+1
		while(low>=0 and high<len(s) and s[low]==s[high]):
			if high-low+1>max_len:
				max_len=high-low+1
				start=low
			low-=1
			high+=1
	return s[start:start+max_len]

def main():
	s=input()
	palin=longest_palin(s)
	print(palin)

if __name__ == '__main__':
	main()