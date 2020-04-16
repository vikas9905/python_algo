def check_vertical(l):
    num1=10e10
    for i in range(len(l)):
        for j in range(len(l[0])-2):
            if l[i].count(l[i][j])>=3:
                num1=min(num1,l[i][j])
    return num1

def check_horizonta(l):
    num=10e10
    l=[[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
    for i in range(len(l)):
        for j in range(len(l[0])-2):
            if l[i].count(l[i][j])>=3:
                num=min(num,l[i][j])
    return num

def check_diagonal(l):
    i=2
    min1=10e10
    min2=10e10
    while(i<len(l)):
        min_ele=10e10
        right_dia=[]
        left_dia=[]
        for j in range(i):
            right_dia.append(l[j][j])
            left_dia.append(l[i-j][j])
        right_set=set(right_dia)
        left_set=set(left_dia)
        for k in right_set:
            c=right_dia.count(k)
            if c>=3:
                if k<min_ele:
                    min_ele=k
        for k in left_set:
            c=left_dia.count(k)
            if c>=3:
                if k<min_ele:
                    min_ele=k
        min1=min(min1,min_ele)
        i+=1
    l=[[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
    min2=min(min2,check_diagonal_left(l))
    return min2


def check_diagonal_left(l):
    i=2
    min1=10e10
    min2=10e10
    while(i<len(l)):
        min_ele=10e10
        right_dia=[]
        left_dia=[]
        for j in range(i):
            right_dia.append(l[j][j])
            left_dia.append(l[i-j][j])
        right_set=set(right_dia)
        left_set=set(left_dia)
        for k in right_set:
            c=right_dia.count(k)
            if c>=3:
                if k<min_ele:
                    min_ele=k
        for k in left_set:
            c=left_dia.count(k)
            if c>=3:
                if k<min_ele:
                    min_ele=k
        min1=min(min1,min_ele)
        i+=1
        return min1




def main():
    n,m=map(int,input().split())
    l=[list(map(int,input().split())) for i in range(n)]
    if n<m:
        diff=m-n
        for i in range(diff):
            l.append([(10e10)]*m)

    num1=check_vertical(l)
    num2=check_horizonta(l)
    num3=check_diagonal(l)
    num=min(num1,num2,num3)
    print(num) if num!=10e10 else print("-1")
if __name__ == '__main__':
    main()