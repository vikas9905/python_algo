arr=list(map(int,input().split()))
stack=[]
next_greater=[0]*(100000)
stack.append(arr[0])
i=1
for i in range(1,len(arr)):
	if len(stack)==0:
		stack.append(arr[i])
	while len(stack)!=0 and stack[-1]<arr[i]:
		next_greater[stack[-1]]=arr[i]
		stack.pop()
	stack.append(arr[i])
	i+=1
while(len(stack)!=0):
	next_greater[stack[-1]]=-1
	stack.pop()
for i in range(len(arr)):
	print("{}------>{}".format(arr[i],next_greater[arr[i]]))



