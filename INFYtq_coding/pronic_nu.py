from itertools import combinations
def check(num):
    i=0
    num=int(num)
    while(i*i<=num):
        if i*(i+1)==num:
            return 1
        i+=1
    return 0

def subString(Str,n): 
    l=[]
    pronic=[]
    # Pick starting point 
    for Len in range(1,n + 1): 
          
        # Pick ending point 
        for i in range(n - Len + 1): 
              
            # Print characters from current 
            # starting point to current ending 
            # point.  
            j = i + Len - 1
            st=''
            for k in range(i,j + 1): 
                st+=Str[k]
            l.append(int(st))
    SET=set(l)
    l1=list(SET)
    for i in l1:
        if check(i)==1:
            pronic.append(i)
    pronic.sort()
    return pronic
arr=input()
pronic=subString(arr,len(arr))
print(*pronic)
        
            