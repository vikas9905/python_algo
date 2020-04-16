def check_anagram_count(txt,pat):
	txtArr=[0]*256
	patArr=[0]*256
	count=0
	for i in range(len(pat)):
		txtArr[ord(txt[i])]+=1
		patArr[ord(pat[i])]+=1
	for i in range(len(pat),len(txt)):
		if txtArr==patArr:
			count+=1
		txtArr[ord(txt[i-len(pat)])]-=1
		txtArr[ord(txt[i])]+=1
	if txtArr==patArr:
		count+=1
	return count

def main():
	txt=input()
	pat=input()
	res=check_anagram_count(txt,pat)
	print(res)

if __name__ == '__main__':
	main()