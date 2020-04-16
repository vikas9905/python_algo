class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class single_list:
	def __init__(self):
		self.head=None
def Insert(data,obj):
	if obj.head==None:
		obj.head=node(data)
		return obj.head
	tmp=obj.head
	while(tmp.next!=None):
		tmp=tmp.next
	new_data=node(data)
	tmp.next=new_data
	return obj.head
def delete(data,obj):
	if(data==obj.head.data):
		tmp=obj.head.next
		obj.head.next=None
		return tmp
	else:
		tmp=obj.head
		while(tmp.next.data!=data):
			tmp=tmp.next
		p=tmp.next
		tmp.next=tmp.next.next
		p.next=None
		return obj.head

def Print(head):
	while head !=None:
		print(head.data)
		head=head.next
if __name__=='__main__':
	data=int(input('Enter -1 to terminate '))
	obj=single_list()
	while (1):
		if(data==-1):
			break
		head=Insert(data,obj)
		data=int(input())
	Print(head)
	data=int(input("enter data to delete "))
	head=delete(data,obj)
	Print(head)
