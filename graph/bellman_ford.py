import queue
class Graph:
	def __init__(self,vertex):
		self.vertex=vertex
		self.list1=[[] for _ in range(vertex)]
	def add_edge(self,src_dest_wt):
		self.list1[src_dest_wt[0]].append(src_dest_wt[1:])
	def bellman_ford(self,src,edge):
		dist=[(10e10)]*self.vertex
		dist[src]=0
		for i in range(1,self.vertex):
			for j in range(0,edge):
				source=j
				dest=self.list1[source][0]
				wt=self.list1[source][1]
				if dist[dest]>dist[source]+wt and dist[source]!=(10e10):
					dist[dest]=dist[source]+wt
		for i in range(self.vertex):
			print(i,dist[i],sep="\t")
	
	def printpath(self,parent,j):
		if(parent[j]==-1):
			return
		self.printpath(parent,parent[j])
		print(j)
		
		#print(c)
	def adjlist(self):
		for i in range(len(self.list1)):
			print(i,":->",end=' ')
			for j in self.list1[i]:
				print(j,end=' ')
			print()

def main():
	vertex=int(input("enter number of vertex"))
	obj=Graph(vertex)
	edge=int(input("enter nu of edges"))
	while(edge>0):
		src_dest_wt=list(map(int,input().split()))
		obj.add_edge(src_dest_wt)
		edge-=1
	src=int(input("enter source\n"))
	obj.bellman_ford(src,edge)
	obj.adjlist()
if __name__ == '__main__':
	main()