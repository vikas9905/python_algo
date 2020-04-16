def find_xseries(arr):
	n=len(arr)
	ans_list=[]
	for i in range(len(arr)-1):
		ll=[arr[i],arr[i+1]]
		k=2
		while(True):
			Sum=ll[k-1]+ll[k-2]
			if Sum in arr:
				ll.append(Sum)
				k+=1
			else:
				break
		#print(ll)
		if(len(ans_list)<len(ll)):
			ans_list=ll
		elif len(ans_list)>len(ll):
			continue
		else:
			for i in range(len(ans_list)):
				if ans_list[i]>ll[i]:
					ans_list=ll
				elif ans_list[i]==ll[i]:
					continue
				else:
					break
	return ans_list

def main():
	arr=list(map(int,input().split(',')))
	ans_list=[]
	arr.sort()
	ans_list=find_xseries(arr)
	print(*ans_list[0:len(ans_list)-1],sep=",")

if __name__ == '__main__':
	main()