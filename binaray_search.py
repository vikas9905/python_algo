import bisect
arr=list(map(int,input().split()))
data=int(input())
def binary_by_stl(arr,data):
    index=bisect.bisect_left(arr,data)
    if(index<len(arr)):
        return index
    else:
        return -1
def binary_search(l,r,arr,data):
    if(r>=l):
        mid=int((r+l)/2)
        if arr[mid]==data:
            return mid
        elif(arr[mid]>data):
            return(l,mid-1,arr,data)
        else:
            return(mid+1,r,arr,data)
    else:
        return -1
if __name__=='__main__':
    arr.sort()
    index=binary_by_stl(arr,data)
    i=binary_search(0,len(arr)-1,arr,data)
    if index==-1 or i==-1:
        print("not found")
    else:
        print(index,i,type(i))
