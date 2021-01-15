class Node:
	def __init__(self, data=None, next = None):
		self.data = data
		self.next = next

	def print(self):
		print(self.data)
