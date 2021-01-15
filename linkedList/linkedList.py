from node import Node
import random

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		if not self.head:
			self.head = Node(data)
			return
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = Node(data)
			
	def print(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

	def search(self, target):
		current = self.head
		while current != None:
			if current.data == target:
				print("Found it!")
				current.print()
				return True
			else:
				current = current.next
		print("Not Found!")
		return False
		
ll = LinkedList()

for i in range(0, 20):
	i = random.randint(1, 30)
	ll.append(i)
	
ll.print()
ll.search(10)
	
