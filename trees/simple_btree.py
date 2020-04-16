class Node:
	def __init__(self,data=0):
		self.data=data
		self.right=None
		self.left=None

def Inorder(node):
	if(node==None):
		return
	Inorder(node.left)
	print(node.data)
	Inorder(node.right)

def main():
	root=None
	n=int(input("enter nu of data\n"))
	data=input("enter data\n")
	root=Node(data)
	root1=root
	i=1
	while(n>1):
		i+=1
		n-=1
		data=input("enter data\n")
		if(i%2!=0):
			root1.left=Node(data)
			root1=root1.left
		else:
			root1.right=Node(data)
			root1=root1.right
	Inorder(root)
if __name__ == '__main__':
	main()