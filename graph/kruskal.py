from collections import defaultdict
class Graph:
	def __init__(self,vertex):
		self.list1=[[]*vertex for _ in range(vertex)]
		self.graph=[]
	def add_edge(self,weight_src_dest):
		self.graph.append(weight_src_dest)
	def Find(self,arr,i):
		if arr[i]==-1:
			return i
		return self.Find(arr,arr[i])
	def Union(self,arr,src,dest):
		x=self.Find(arr,src)
		y=self.Find(arr,dest)
		if x!=y:
			arr[x]=y
		return arr
	def kruskal(self,edge_nu):
		self.arr=[-1]*edge_nu
		self.arr1=[]
		self.mincost=0
		self.graph=sorted(self.graph,key=lambda item:item[2])
		for i in range(edge_nu):
			self.src=self.graph[i][0]
			self.dest=self.graph[i][1]
			self.wt=self.graph[i][2]
			print(self.src,self.dest,self.wt,sep=" ")
			if self.Find(self.arr,self.src) !=self.Find(self.arr,self.dest):
				self.mincost+=self.wt
				self.arr=self.Union(self.arr,self.src,self.dest)
		print(self.arr)
		return self.mincost #,self.arr
def main():
	vertex=int(input())
	edge_nu=int(input())
	edge_=edge_nu
	obj=Graph(vertex)
	while (edge_nu):
		src_dest_wt=list(map(int,input().split()))
		obj.add_edge(src_dest_wt)
		edge_nu-=1
	mincost=obj.kruskal(edge_)
	print(mincost)
	#print(arr)
if __name__ == '__main__':
	main()