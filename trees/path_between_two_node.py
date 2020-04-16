class Node:
	def __init__(self):
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

def getpath(root,path_arr,n):
	if root==None:
		return 0
	path_arr.append(root.data)
	if n==root.data:
		return 1
	if getpath(root.left,path_arr,n) or getpath(root,path_arr,n):
		return 1
	path_arr.pop()
	return 0

def path_between_node(root,n1,n2):
	path1=[]
	path2=[]
	getpath(root,path1,n1)
	getpath(root,path2,n2)
	print(path1)
	print(path2)

def main():
	n=int(input())
	arr=list(map(int,input().split()))
	root=None
	root=Insert(root,arr[0])
	node1,node2=map(int,input().split())
	ans=path_between_node(root,node1,node2)

