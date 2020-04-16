class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
def create_bst(arr):
	if len(arr)==0:
		return None
	mid=len(arr)//2
	root=Node(arr[mid])
	root.left=create_bst(arr[:mid])
	root.right=create_bst(arr[mid+1:])
	return root
def preorder(root):
	if root==None:
		return
	print(root.data,end=" ")
	preorder(root.left)
	
	preorder(root.right)

def height_of_tree(root):
	if root==None:
		return 0
	l=height_of_tree(root.left)
	r=height_of_tree(root.right)
	return max(l,r)+1

def main():
	arr=list(map(int,input().split()))
	arr.sort()
	root=create_bst(arr)
	preorder(root)
	h=height_of_tree(root)
	print(h)
main()