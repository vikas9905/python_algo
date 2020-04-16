def All_permutation(s,l,r):
    if l==r:
        print(tostring(s))
    else:
        for i in range(l,r+1):
            s[i],s[l]=s[l],s[i]
            All_permutation(s,l+1,r)
            s[i],s[l]=s[l],s[i]
def tostring(s):
    return ''.join(s)

def main():
    t=int(input())
    while(t):
        s=input()
        l=list(s)
        All_permutation(l,0,len(s)-1)
        t-=1
if __name__ == '__main__':
    main()