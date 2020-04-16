f=open('q2.txt','r')
ans=open('q2_ans.txt','a+')
n,k=f.readline().split(' ')
n=int(n)
k=int(k)
arr=list(map(int,f.readline().split(' ')))
def binary(arr,k):
    an=0
    Sum=0
    for i in range(len(arr)):
        Sum+=arr[i]
        if Sum<k:
            an=(i+1)
        else:
            break
    return an
an=binary(arr,k)
ans.write(str(an))
print(ans)