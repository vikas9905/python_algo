n=int(input())
def triangle():
	for i in range(n):
		print((chr(ord('A')+i)+' ')*(i+1),sep=' ')
def reverse_triangle():
	for i in range(n):
		print('* '*(n-i))
def reverse_num():
	for i in range(n):
		for j in range(n-i):
			print(j+1,end=' ')
		print("\n")
def pyramid():
	for i in range(n):
		print(" "*(n-i-1),(str(i+1)+" ")*(i+1))
def alpha_pyramid():
	for i in range(n):
		c=0
		for j in range(i+1):
			if c==0:
				print(" "*(n-i-1),end='')
				c+=1
			print(((chr(ord('A')+(n-j-1)))),end=' ')
		print()
def right_pyramid():
	for i in range(n):
		for j in range(0,i+1):
			print(chr(ord('A')+j),end=' ')
		print()
	for i in range(n-1,0,-1):
		for j in range(0,i):
			print(chr(ord('A')+j),end=' ')
		print()
def down_pyramid():
	for i in range(n):
		print(" "*i,end='')
		for j in range(0,n-i):
			print(chr(ord('A')+j),end=' ')
		print()
def diamond():
	for i in range(n):
		print(" "*(n-i-1),end='')
		for j in range(0,i+1):
			print("*",end=" ")
		print()
	for i in range(n-1,0,-1):
		print(" "*(n-i),end='')
		for j in range(0,i):
			print("*",end=" ")
		print()
def right_star():
	for i in range(n):
		print("* "*(i+1))
	#print()
	for i in range(n-1,0,-1):
		print("* "*(i))
def left_start():
	for i in range(n):
		print(" "*(n-i-1),"*"*(i+1),sep=" ")
	for i in range(n-1,0,-1):
		print(" "*(n-i-1),"*"*(i+1))
def hut():
	print("\n")
	print(" "*(n+1),"*")
	for i in range(n):
		print(" "*(n-i-1),"*"*1," "*(2*i+1),"*")
def down_hut():
	print("\n")
	#print(" "*(n+1),"*")
	for i in range(n-1,0,-1):
		print(" "*(n-i-1),"*"*1," "*(2*i+1),"*")
	print(' '*n,"*")

if __name__ == '__main__':
	triangle()
	reverse_triangle()
	reverse_num()
	pyramid()
	alpha_pyramid()
	right_pyramid()
	down_pyramid()
	diamond()
	right_star()
	left_start()
	hut()
	down_hut()
