## imports 


## Classes 
class Node: 
	def __init__(self,dataval=None):
		self.dataval = dataval
		self.nextval = None

class LinkedList:
	
	def __init__(self):
		self.headval = None
	
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval 

	## code to insert at the beginning of list
	
	## code to insert at the end of the list

	## code to return length of list 

	## code to insert at postion in list

	## 

if __name__=='__main__':
	ll = LinkedList()
	ll.headval = Node("Mon")
	e2 = Node("Tue")
	e3 = Node("Wed")
	
	# Link first Node to second node
	list.headval.nextval = e2
	
	# Link second Node to third node
	e2.nextval = e3 
        
	# print out linked list
	list.listprint() 
