class graph:
	def __init__(self,v):
		self.ver=v+1
		self.l=[[] for _ in range(v+1)]
		self.time=0
		self.child=[0]*(v+1)
	def add_edge(self,x,y):
		self.l[x].append(y)
		self.l[y].append(x)
	def APUtil(self,visited,disc,low,parent,ap,u):
		visited[u]=1
		children=0
		disc[u]=self.time
		low[u]=self.time
		self.time+=1

		for i in self.l[u]:
			if visited[i]==0:
				parent[i]=u
				children+=1
				self.APUtil(visited,disc,low,parent,ap,i)
				low[i]=min(low[i],low[u])
				if parent[u]==-1 and children>1:
					ap[u]=1
					self.child[u]=children
				if parent[u]!=-1 and disc[u]<=low[i]:
					ap[u]=1
					self.child[u]=children
			elif i!=parent[u]:
				low[u]=min(low[u],disc[i])

	def articulation_point(self):
		visited=[0]*(self.ver)
		disc=[float('Inf')]*(self.ver)
		low=[float('Inf')]*(self.ver)
		parent=[-1]*self.ver
		ap=[-1]*self.ver
		for i in range(self.ver):
			if visited[i]==0:
				self.APUtil(visited,disc,low,parent,ap,i)
		return ap
	def count_child(self,src,ap):
		cnt=1
		for i in self.l[src]:
			if ap[i]!=1:
				cnt+=1
		return cnt

def main():
	v,e=map(int,input().split())
	total=0
	obj=graph(v)
	obj.add_edge(0,0)
	even=0
	odd=0
	for i in range(e):
		x,y=map(int,input().split())
		obj.add_edge(x,y)
	ap=obj.articulation_point()
	for i in range(len(ap)):
		if ap[i]==1:
			total+=1
			cnt=obj.count_child(i,ap)
			if cnt%2!=0:
				odd+=1
			else:
				even+=1
	if odd==0:
		print("1 0")
	if even==0:
		print("0 1")
	else:
		print(even//total,end=" ")
		print(odd//total)
main()
