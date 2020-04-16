def leivdistance(str1,str2,m,n):
	if m==0:
		return len(str2)
	if n==0:
		return len(str1)
	if str1[m-1]==str2[n-1]:
		return leivdistance(str1,str2,m-1,n-1)
	return 1+min(leivdistance(str1,str2,m,n-1),leivdistance(str1,str2,m-1,n),leivdistance(str1,str2,m-1,n-1))
def main():
	str1=input()
	str2=input()
	print(leivdistance(str1,str2,len(str1),len(str2)))
if __name__ == '__main__':
	main()
