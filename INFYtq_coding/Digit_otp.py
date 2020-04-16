n=input()
s=n[1::2]
ans=''
for i in s:
	ans+=str(int(i)*int(i))
print(ans[0:4])

