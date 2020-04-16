def solve(maze):
	soln=[[0]*4 for _ in range(4)]
	if mazeUtil(maze,soln,0,0)==False:
		print("soln not exists")
		return False
	print_soln(soln)
	return True
def mazeUtil(maze,soln,x,y):
	if x==4-1 and y==4-1:
		soln[x][y]=1
		return True
	if is_safe(maze,x,y)==True:
		soln[x][y]=1
		if mazeUtil(maze,soln,x+1,y)==True:
			return True
		if mazeUtil(maze,soln,x,y+1)==True:
			return True
		soln[x][y]=0
		return False
def print_soln(soln):
	for i in soln:
		for j in i:
			print(j,end=" ")
		print()
def is_safe(maze,x,y):
	if x>=0 and x<4 and y>=0 and y<4 and maze[x][y]==1:
		return True
	return False

def main():
	maze=[[1,0,0,0],
	[1,1,0,1],
	[0,1,0,0],
	[1,1,1,1]]
	solve(maze)

if __name__ == '__main__':
	main()