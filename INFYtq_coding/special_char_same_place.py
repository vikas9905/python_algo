import re
s=input()
p=re.compile('[0-9,a-z]')
s2=''.join(p.findall(s))
s2=s2[::-1]
new_s=''
j=0
for i in s:
	if ord(i)>=ord('a') and ord(i)<=ord('z') or ord(i)>=ord('0') and ord(i)<=ord('9'):
		new_s=new_s+s2[j]
		j+=1
		continue
	new_s=new_s+i
print(new_s)

