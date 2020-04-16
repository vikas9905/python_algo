class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def Insert(node,data):
	if(node==None):
		return Node(data)
	elif node.data>data:
		if node.left!=None:
			Insert(node.left,data)
		else:
			node.left=Insert(node.left,data)
	else:
		if(node.right!=None):
			Insert(node.right,data)
		else:
			node.right=Insert(node.right,data)

def Inorder(node):
	if(node==None):
		return
	Inorder(node.left)
	print(node.data)
	Inorder(node.right)
def remove(node,data):
	if node==None:
		return
	elif node.data>data:
		remove(node.left,data)
	elif node.data<data:
		remove(node.right,data)
	else:
		if(node.right==None):
			temp=node.left
			node=None
			return temp
		else:
			temp=node.right
			node=None
			return temp
	
def main():
	n=int(input("enter nu of element\n"))
	data=int(input("enter data\n"))
	root=None
	root=Insert(root,data)
	while(n>1):
		n-=1
		data=int(input("enter data\n"))
		Insert(root,data)
	#Inorder(root)
	root=remove(root,12)
	Inorder(root)
if __name__ == '__main__':
	main()