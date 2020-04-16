def LCS(txt,pat):
	table=[[0]*(len(pat)+1) for _ in range(len(txt)+1)]
	for i in range(len(txt)+1):
		for j in range(len(pat)+1):
			if i==0 or j==0:
				table[i][j]=0
			elif txt[i-1]==pat[j-1]:
				table[i][j]=table[i-1][j-1]+1
			else:
				table[i][j]=max(table[i-1][j],table[i][j-1])
	
	return table[len(txt)][len(pat)]

def main():
	txt=input()
	pat=input()
	size=LCS(txt,pat)
	print("size={}".format(size))
if __name__ == '__main__':
	main()