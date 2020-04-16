import heapq
import queue
class Node:
	def __init__(self,freq,data=None):
		self.data=data
		self.freq=freq
		self.right=None
		self.left=None
class Hauffman:
	def __init__(self,prior_queue):
		self.prior_queue=prior_queue
	def make_tree(self):
		while self.prior_queue.qsize()!=1:
			a=self.prior_queue.get()
			b=self.prior_queue.get()
			NodeA=Node(a[0]+b[0])
			if type(a[1])!=type(''):
				if a[0]<b[0]:
					NodeA.left=a[1]
				else:
					NodeA.right=a[1]
			else:
				nodea=Node(a[0],a[1])
				if a[0]<b[0]:
					NodeA.left=nodea
				else:
					NodeA.right=nodea

			if type(b[1])!=type(''):
				if(b[0]<a[0]):
					NodeA.left=b[1]
				else:
					NodeA.right=b[1]
			else:
				nodea=Node(b[0],b[1])
				if b[0]<a[0]:
					NodeA.left=nodea
				else:
					NodeA.right=nodea
			self.prior_queue.put((a[0]+b[0],NodeA))
			if(self.prior_queue.qsize()==1):
				break
		return self.prior_queue
	def  get_code(self,root,arr,top):
		if root==None:
			return
		self.get_code(root.left,arr,top)
		print(root.data)
		self.get_code(root.right,arr,top
			)
	def print_code(self,arr,top):
		for i in arr:
			print(i)

def main():
	n=int(input("enter nu of char\n"))
	l=[-1]*n
	top=0
	prior_queue=queue.PriorityQueue()
	while(n):
		a,freq=input().split()
		prior_queue.put((int(freq),a))
		n-=1

	obj=Hauffman(prior_queue)
	root=obj.make_tree()
	print(root.get())
	obj.get_code(root.get()[1],l,top)
	#obj.print_code(l,top)
if __name__ == '__main__':
	main()
