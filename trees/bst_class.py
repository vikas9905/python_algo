class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

class Tree:
	root=None
	root2=None
	def Insert(self,data,root):
		if(root==None):
			return Node(data)
		elif root.data>data:
			if root.left!=None:
				self.Insert(data,root.left)
			else:
				root.left=self.Insert(data,root.left)
		else:
			if root.right!=None:
				self.Insert(data,root.right)
			else:
				root.right=self.Insert(data,root.right)
	def Preorder(self,root):
		if root==None:
			return
		print(root.data)
		self.Preorder(root.left)
		self.Preorder(root.right)
	def Iterative_preorder(self,root):
		stack=[]
		result=[]
		stack.append(root)
		while len(stack)!=0:
			node=stack.pop()
			result.append(node.data)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		print(result)
	def Inorder(self,root):
		if root==None:
			return
		self.Inorder(root.left)
		print(root.data)
		self.Inorder(root.right)
	def Iterative_Inorder(self,root):
		node=root
		result=[]
		stack=[]
		while stack or node:
			if node:
				stack.append(node)
				node=node.left
			else:
				node=stack.pop()
				result.append(node.data)
				node=node.right
	def postoredr(self,root):
		if(root==None):
			return
		postoredr(root.left)
		postoredr(root.right)
		print(root.data)
	def Iterative_postorder(self,root):
		pass
	def level_order_traverse(self,root):
		pass
	def search(self,data,root):
		if root==None:
			print("no data found")
			return
		elif root.data>data:
			search(data,root.left)
		elif root.data<data:
			search(data,root.right)
		else:
			print("data found")
	def size_of_tree(self,root):
		if(root==None):
			return 0
		else:
			return size_of_tree(root.left)+size_of_tree(root.right)+1
	def max_depth(self,root):
		if(root==None):
			return 0
		else:
			return max(max_depth(root.left),max_depth(root.right))+1
	def nu_of_child(self,root):
		pass
	def nu_of_full_binary_tree(self,root):
		pass
	def structure_equal(self,root1,root1):
		pass
	def create_two_tree(self,root):
		pass
	def sum_of_all_node(self,root):
		pass
	def mirror_of_tree(self,root):
		pass
	def are_given_two_tree_mirror_of_each_other(self,root1,root2):
		pass
	def find_lca(self,data1,data2,root):
		if root ==None:
			return
		if root.data=data1 or root.data=data2:
			return root
		left_check=find_lca(data1,data1,root.left)
		right_check=find_lca(data1,data2,root.right)
		if left_check and right_check:
			return root
		return left if left_check is not None else right_check
	def zig_zag_traverse(self,root):
		if root is None:
			return
		current=[]
		next_level=[]
		l_to_r=True
		current.append(root)
		while len(current)>0:
			node=current.pop()
			print(node.data)
			if l_to_r:
				if root.left:
					next_level.append(root.left)
				if root.right:
					next_level.append(root.right)
			else:
				if root.right:
					next_level.append(root.right)
				if root.left:
					next_level.append(root.left)
			if len(current)==0:
				next_level,current=current,next_level



def main():
	print("1.insert\t",end='')
	print("2.Inorder traverse\t 3.Iterative_Inorder")
	print("4.Preorder\t 5.preoredr by Iterative_preorder\t",end='')
	print("6.postoredr\t 7.Iterative_postorder")
	print("8.level_order_traverse\t 9.search data")
	print("10.size_of_tree\t 11.max_depth")
	print("12.nu_of_child\t 13.nu_of_full_binary_tree")
	print("14.structure_equal\t 15.create_two_tree")
	print("16. sum_of_all_node\t 17.mirror_of_tree")
	print("enter 0")
	print("enter your choice\n")
	while(True):
		choice=int(input())
		if choice==1:
			n=int(input("enter nu of data to add\n"))
			data=int(input("enter data\n"))
			Tree.root=Node(data)
			while(n>1):
				global obj
				obj =Tree()
				data=int(input("enter data\n"))
				obj.Insert(data,Tree.root)
				n-=1
		elif choice==2:
			obj.Inorder(Tree.root)
		elif choice==3:
			obj.Iterative_Inorder(Tree.root)
		elif choice==4:
			obj.Preorder(Tree.root)
		elif choice==5:
			obj.Iterative_preorder(Tree.root)
		elif choice==15:
			n=int(input("enter nu of data to add\n"))
			data=int(input("enter data\n"))
			Tree.root2=Node(data)
			while(n>1):
				global obj1
				obj1 =Tree()
				data=int(input("enter data\n"))
				obj1.Insert(data,Tree.root)
				n-=1
		elif choice==0:
			break
		else:
			obj.Iterative_preorder(Tree.root)
if __name__ == '__main__':
	main()