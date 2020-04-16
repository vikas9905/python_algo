class Graph:
	def __init__(self,vertex):
		self.vertex=vertex
		self.list1=[[] for _ in range(vertex)]
	def add_edge(self,src,dest):
		self.list1[src].append(dest)

	def DfsUtil(self,src,visited):
		visited[src]=True
		for i in self.list1[src]:
			if(visited[i]==False):
				self.DfsUtil(i,visited)

	def transpose(self):
		self.g=Graph(self.vertex)
		for i in range(self.vertex):
			for j in self.list1[i]:
				self.list1[j].append(i)
		return self.g


	def is_strongly_connected(self,src):
		visited=[False]*self.vertex
		self.DfsUtil(src,visited)
		for i in range(self.vertex):
			if visited[i]==False:
				return False
		g=self.transpose()
		visited=[False]*self.vertex
		self.DfsUtil(src,visited)
		for i in range(self.vertex):
			if visited[i]==False:
				return False
		return True

def main():
	vertex=int(input("enter number of vertex"))
	obj=Graph(vertex)
	edge=int(input("enter nu of edges"))
	while(edge>0):
		src,dest=map(int,input().split())
		obj.add_edge(src,dest)
		edge-=1
	res=obj.is_strongly_connected(src)
	print(res)

if __name__ == '__main__':
	main()
