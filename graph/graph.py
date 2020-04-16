import queue
class Graph:
	def __init__(self,vertex):
		self.list1=[[] for _ in range(vertex)]
		self.vertex=vertex
		self.graph=[[0]*vertex for _ in range(vertex)]
	def add_edge(self,src,dest):
		self.graph[src][dest]=1
		self.graph[dest][src]=1
		self.list1[src].append(dest)
	def disp(self):
		for i in range(len(self.graph)):
			print(i," :",end='')
			for j in self.graph[i]:
				print(j,end='')
			print()
	def adjlist(self):
		for i in range(len(self.list1)):
			print(i,":->",end=' ')
			for j in self.list1[i]:
				print(j,end=' ')
			print()
	def dfs_traverse(self):
		pass
	def bfs_traverse(self,src):
		visited=[0]*self.vertex
		q=queue.Queue()
		q.put(src)
		visited[src]=True
		while q.empty()==False:
			f=q.get()
			print(f,end=" ")
			for i in self.list1[f]:
				if visited[i]==False:
					visited[i]=True
					q.put(i)
	def dfs_util(self,src,visited):
		visited[src]=True
		print(src,end=" ")
		for i in self.list1[src]:
			if visited[i]==False:
				self.dfs_util(i,visited)

	def dfs(self,src):
		visited=[0]*self.vertex
		self.dfs_util(src,visited)

	def cycle_util(self,src,visited,recr):
		visited[src]=True
		recr[src]=True
		for i in self.list1[src]:
			if visited[i]==False:
				if self.cycle_util(i,visited,recr)==True:
					return True
				if recr[i]==True:
					return True
		recr[i]=False
		return False

	def detect_cycle(self):
		self.visited=[0]*self.vertex
		self.recr=[0]*self.vertex
		for i in range(self.vertex):
			if self.visited[i]==False:
				if self.cycle_util(i,self.visited,self.recr)==True:
					return True

		return False
	
def main():
	vertex=int(input("enter number of vertex"))
	obj=Graph(vertex)
	edge=int(input("enter nu of edges"))
	while(edge>0):
		src,dest=map(int,input().split())
		obj.add_edge(src,dest)
		edge-=1
	src=int(input("enter source\n"))
	obj.disp()
	obj.bfs_traverse(src)
	print()
	obj.dfs(src)
	print()
	print(obj.detect_cycle())
	obj.adjlist()
if __name__ == '__main__':
	main()
