'''Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.

Examples :

Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  "AGXGTXAYB" '''

def find_supersequence(s1,s2,n,m):
	if not n:
		return m
	if not m:
		return n
	if s1[n-1]==s2[m-1]:
		return 1+find_supersequence(s1,s2,n-1,m-1)
	return 1+min(find_supersequence(s1,s2,n-1,m),find_supersequence(s1,s2,n,m-1))



def main():
	s=input()
	s2=input()
	print(find_supersequence(s,s2,len(s),len(s2)))
if __name__ == '__main__':
	main()
