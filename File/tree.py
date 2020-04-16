import sys
sys.setrecursionlimit(10**6)
tree_path=open('tree_path.txt','r')
ans=open('tree_path_ans.txt','a+')
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def Insert(root,data):
    if root==None:
        return Node(data)
    elif root.data>=data:
        if root.left!=None:
            Insert(root.left,data)
        else:
            root.left=Insert(root.left,data)
    else:
        if root.right!=None:
            Insert(root.right,data)
        else:
            root.right=Insert(root.right,data)

def getpath(root,n,path1):

    if root==None:
        return 0
    path1.append(root.data)
    if root.data==n:
        return 1
    if getpath(root.left,n,path1) or getpath(root.right,n,path1):
        return 1
    path1.pop()
    return 0
def path_between_node(root,n1,n2):
    path1=[]
    path2=[]
    getpath(root,n1,path1)
    getpath(root,n2,path2)
    ans.write(str(path1))
    ans.write(str(path2))
    if n1<=root.data and n2>=root.data:
        return max(max(path1),max(path2))
    elif n1<=root.data and n2<=root.data:
        return max(path1)
    elif n1>=root.data and n2>=root.data:
        return max(path2)
def main():
    n=int(tree_path.readline())
    arr=list(map(int,tree_path.readline().split()))
    root=None
    root=Insert(root,arr[0])
    for i in range(1,n):
        Insert(root,arr[i])
    node1,node2=map(int,tree_path.readline().split())
    ans.write(str(path_between_node(root,node1,node2)))
    print(ans)
main()

