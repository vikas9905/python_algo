import queue
class Graph:
	def __init__(self,vertex):
		self.vertex=vertex
		self.list1=[[] for _ in range(vertex)]
	def add_edge(self,src_dest_wt):
		self.list1[src_dest_wt[0]].append(src_dest_wt[1:])
		self.list1[src_dest_wt[1]].append(src_dest_wt[0::2])

	def dijkstra(self,src):
		dist=[int(10e10)]*self.vertex
		parent=[-1]*self.vertex
		dist[src]=0
		
		q=queue.PriorityQueue()
		q.put((0,src))
		c=0
		while(q.empty()==False):
			u=q.get()[1]
			#print(u)
			for i in self.list1[u]:
				v=i[0]
				wt=i[1]
				#print(dist[v],dist[u]+wt)
				if dist[v]>dist[u]+wt:
					dist[v]=dist[u]+wt
					q.put((dist[v],v))
					parent[v]=u
					c+=1
		print("vertex\t distance from source")
		for i in range(self.vertex):
			print(i,dist[i],sep="\t")
			#self.printpath(parent,i)
		print("\n",parent)
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
	obj.dijkstra(src)
	obj.adjlist()
if __name__ == '__main__':
	main()