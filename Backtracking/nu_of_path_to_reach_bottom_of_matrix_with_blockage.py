
def count_path_maze(maze):
	if maze[0][0]==-1:
		return 0
	#initializing leftmost column
	for i in range(len(maze)):
		if maze[i][0]==0:
			maze[i][0]=1
		else:   # if we encountered the block cell
			break
	for i in range(1,len(maze[0])):
		if maze[0][i]==0:
			maze[0][i]=1
		else:
			break
	for i in range(1,len(maze)):
		for j in range(1,len(maze[0])):
			if maze[i][j]==-1:
				continue
			if maze[i-1][j]>0:
				maze[i][j]=maze[i][j]+maze[i-1][j]
			if maze[i][j-1]>0:
				maze[i][j]=maze[i][j]+maze[i][j-1]
	for i in maze:
		for j in i:
			print(j,end=" ")
		print()
	if maze[len(maze)-1][len(maze[0])-1]>0:
		return maze[len(maze)-1][len(maze[0])-1]
	else:
		return 0


def main():
	maze=[[0,0,0,0],
	[0,-1,0,0],
	[-1,0,0,0],
	[0,0,0,0]]
	print(count_path_maze(maze))

if __name__ == '__main__':
	main()